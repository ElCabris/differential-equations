"""Loss functions extracted from entrega-1.ipynb.

Total loss:  L = L_PDE + L_IC + L_BC

- L_PDE : mean squared PDE residual  R = ∂û/∂t − α ∂²û/∂x²
- L_IC  : mean squared error on IC   û(x,0) = sin(πx/L)
- L_BC  : mean squared error on BC   û(0,t) = û(L,t) = 0
"""

from __future__ import annotations

import torch
from .architecture import PINN


def pde_residual(
    model: PINN,
    x: torch.Tensor,
    t: torch.Tensor,
    alpha: float = 0.01,
) -> torch.Tensor:
    """Compute the heat-equation PDE residual via automatic differentiation.

    Extracted verbatim from entrega-1.ipynb.

    Args:
        model: PINN network (must be in train mode for create_graph).
        x:     Spatial collocation points, shape (N, 1).  Leaf tensor.
        t:     Temporal collocation points, shape (N, 1). Leaf tensor.
        alpha: Thermal diffusivity.

    Returns:
        R = u_t − α·u_xx,  shape (N, 1).
    """
    x.requires_grad_(True)
    t.requires_grad_(True)

    u = model(x, t)

    u_t = torch.autograd.grad(
        u, t, torch.ones_like(u), create_graph=True
    )[0]
    u_x = torch.autograd.grad(
        u, x, torch.ones_like(u), create_graph=True
    )[0]
    u_xx = torch.autograd.grad(
        u_x, x, torch.ones_like(u_x), create_graph=True
    )[0]

    return u_t - alpha * u_xx


def compute_loss(
    model: PINN,
    x_pde: torch.Tensor,
    t_pde: torch.Tensor,
    x_ic: torch.Tensor,
    t_ic: torch.Tensor,
    u_ic: torch.Tensor,
    x_bc: torch.Tensor,
    t_bc: torch.Tensor,
    alpha: float,
) -> tuple[torch.Tensor, dict[str, float]]:
    """Compute composite PINN loss (from entrega-1.ipynb).

    Returns:
        loss:       Scalar total loss tensor.
        components: Individual loss values for logging.
    """
    mse_pde = torch.mean(pde_residual(model, x_pde, t_pde, alpha) ** 2)
    mse_ic = torch.mean((model(x_ic, t_ic) - u_ic) ** 2)
    mse_bc = torch.mean(model(x_bc, t_bc) ** 2)

    loss = mse_pde + mse_ic + mse_bc
    return loss, {
        "pde": mse_pde.item(),
        "ic": mse_ic.item(),
        "bc": mse_bc.item(),
    }
