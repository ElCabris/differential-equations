from __future__ import annotations

import time
from pathlib import Path

import numpy as np

from app.pinn import trainer
from app.schemas.requests import PINNRequest, PINNResponse

SAVED_MODEL_PATH = Path(__file__).parent.parent.parent / "saved_models" / "heat_pinn.pt"


def solve(req: PINNRequest) -> PINNResponse:
    """Resolve via PINN: load pretrained or train from scratch.

    Decision tree:
      1. load_pretrained=True AND model file exists → load it.
      2. train=True                                 → train a new model.
      3. Neither                                    → raise ValueError.
    """
    if req.load_pretrained and SAVED_MODEL_PATH.exists():
        return _load_and_evaluate(req)

    if req.train:
        return _train_and_evaluate(req)

    raise ValueError(
        "No pretrained model found at saved_models/heat_pinn.pt and train=False. "
        "Either set train=True to train a new model, or provide a pretrained model."
    )


# ── Private helpers ────────────────────────────────────────────────────────────

def _load_and_evaluate(req: PINNRequest) -> PINNResponse:
    t0 = time.perf_counter()
    model, _ = trainer.load(SAVED_MODEL_PATH)

    x = np.linspace(0.0, req.L, req.Nx)
    t = np.linspace(0.0, req.T, req.Nt)
    u = trainer.evaluate_on_grid(model, x, t)

    return PINNResponse(
        x=x.tolist(),
        t=t.tolist(),
        u=u.tolist(),
        loss_history=[],
        training_time=time.perf_counter() - t0,
        loaded_pretrained=True,
    )


def _train_and_evaluate(req: PINNRequest) -> PINNResponse:
    model, loss_history, training_time = trainer.train(
        alpha=req.alpha,
        L=req.L,
        T=req.T,
        epochs=req.epochs,
        lr=req.lr,
        use_lbfgs=req.use_lbfgs,
        save_path=SAVED_MODEL_PATH,
    )

    x = np.linspace(0.0, req.L, req.Nx)
    t = np.linspace(0.0, req.T, req.Nt)
    u = trainer.evaluate_on_grid(model, x, t)

    return PINNResponse(
        x=x.tolist(),
        t=t.tolist(),
        u=u.tolist(),
        loss_history=loss_history,
        training_time=training_time,
        loaded_pretrained=False,
    )
