"""PINN training routines extracted from entrega-1.ipynb.

Two-phase strategy (identical to notebook):
    Phase 1 – Adam:  fast global convergence
    Phase 2 – LBFGS: second-order fine-tuning
"""

from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import torch

from .architecture import PINN
from .losses import compute_loss


# ── Training data ─────────────────────────────────────────────────────────────

def build_training_data(
    alpha: float,
    L: float,
    T: float,
    N_ic: int = 500,
    N_bc: int = 500,
    N_pde: int = 10_000,
) -> dict[str, torch.Tensor]:
    """Build IC, BC and PDE collocation datasets (from entrega-1.ipynb).

    IC:  u(x, 0) = sin(πx/L)
    BC:  u(0, t) = u(L, t) = 0
    PDE: random uniform points inside the domain
    """
    # Initial condition
    x_ic = torch.linspace(0, L, N_ic).view(-1, 1).float()
    t_ic = torch.zeros(N_ic, 1).float()
    u_ic = torch.sin(torch.tensor(np.pi) * x_ic / L).float()

    # Boundary conditions
    t_bc = torch.linspace(0, T, N_bc // 2).view(-1, 1).float()
    x_bc_left = torch.zeros(N_bc // 2, 1).float()
    x_bc_right = torch.full((N_bc // 2, 1), L).float()
    x_bc = torch.cat([x_bc_left, x_bc_right], dim=0)
    t_bc_total = torch.cat([t_bc, t_bc], dim=0)

    # PDE collocation (Monte-Carlo, from notebook)
    x_pde = torch.rand(N_pde, 1) * L
    t_pde = torch.rand(N_pde, 1) * T

    return {
        "x_ic": x_ic,
        "t_ic": t_ic,
        "u_ic": u_ic,
        "x_bc": x_bc,
        "t_bc": t_bc_total,
        "x_pde": x_pde,
        "t_pde": t_pde,
    }


# ── Training ──────────────────────────────────────────────────────────────────

def train(
    alpha: float,
    L: float,
    T: float,
    epochs: int = 2000,
    lr: float = 1e-3,
    use_lbfgs: bool = True,
    save_path: Path | None = None,
) -> tuple[PINN, list[float], float]:
    """Train PINN with Adam + (optionally) LBFGS (from entrega-1.ipynb).

    Args:
        alpha:      Thermal diffusivity.
        L:          Domain length.
        T:          Total time.
        epochs:     Adam iterations.
        lr:         Adam learning rate.
        use_lbfgs:  Whether to apply LBFGS refinement.
        save_path:  If given, save model there after training.

    Returns:
        model:         Trained PINN.
        loss_history:  Per-epoch loss values (downsampled if >1000 pts).
        training_time: Wall time in seconds.
    """
    t0 = time.time()
    model = PINN()
    model.train()

    data = build_training_data(alpha, L, T)
    x_ic, t_ic, u_ic = data["x_ic"], data["t_ic"], data["u_ic"]
    x_bc, t_bc = data["x_bc"], data["t_bc"]
    x_pde, t_pde = data["x_pde"], data["t_pde"]

    loss_history: list[float] = []

    # ── Phase 1: Adam (from notebook) ─────────────────────────────────────────
    optimizer_adam = torch.optim.Adam(model.parameters(), lr=lr)

    for _ in range(epochs):
        optimizer_adam.zero_grad()
        loss, _ = compute_loss(
            model, x_pde, t_pde, x_ic, t_ic, u_ic, x_bc, t_bc, alpha
        )
        loss.backward()
        optimizer_adam.step()
        loss_history.append(loss.item())

    # ── Phase 2: LBFGS (from notebook) ────────────────────────────────────────
    if use_lbfgs:
        optimizer_lbfgs = torch.optim.LBFGS(
            model.parameters(),
            max_iter=50_000,
            tolerance_grad=1e-7,
            line_search_fn="strong_wolfe",
        )

        def closure() -> torch.Tensor:
            optimizer_lbfgs.zero_grad()
            loss, _ = compute_loss(
                model, x_pde, t_pde, x_ic, t_ic, u_ic, x_bc, t_bc, alpha
            )
            loss.backward()
            return loss

        optimizer_lbfgs.step(closure)
        with torch.no_grad():
            final_loss, _ = compute_loss(
                model, x_pde, t_pde, x_ic, t_ic, u_ic, x_bc, t_bc, alpha
            )
        loss_history.append(final_loss.item())

    training_time = time.time() - t0
    model.eval()

    if save_path is not None:
        save(model, save_path, alpha=alpha, L=L, T=T, epochs=epochs, lr=lr)

    # Downsample history to ≤500 points for the API response
    if len(loss_history) > 500:
        step = len(loss_history) // 500
        loss_history = loss_history[::step]

    return model, loss_history, training_time


# ── Persistence ───────────────────────────────────────────────────────────────

def save(model: PINN, path: Path, **metadata: object) -> None:
    """Persist model weights and training metadata to disk."""
    torch.save({"state_dict": model.state_dict(), "metadata": metadata}, path)


def load(path: Path) -> tuple[PINN, dict]:
    """Load PINN from disk.

    Returns:
        model:    Loaded model in eval mode.
        metadata: Dict with training parameters.
    """
    checkpoint = torch.load(path, map_location="cpu")
    model = PINN()
    model.load_state_dict(checkpoint["state_dict"])
    model.eval()
    return model, checkpoint.get("metadata", {})


# ── Grid evaluation ───────────────────────────────────────────────────────────

def evaluate_on_grid(
    model: PINN,
    x: np.ndarray,
    t: np.ndarray,
) -> np.ndarray:
    """Evaluate PINN on a 2-D meshgrid (from entrega-1.ipynb plot_results).

    Args:
        model: PINN in eval mode.
        x:     1-D spatial array, shape (Nx,).
        t:     1-D temporal array, shape (Nt,).

    Returns:
        u: Temperature field, shape (Nt, Nx).
    """
    X, T_grid = np.meshgrid(x, t)  # (Nt, Nx)
    x_flat = torch.tensor(X.flatten(), dtype=torch.float32).view(-1, 1)
    t_flat = torch.tensor(T_grid.flatten(), dtype=torch.float32).view(-1, 1)

    model.eval()
    with torch.no_grad():
        u = model(x_flat, t_flat).numpy().reshape(len(t), len(x))
    return u
