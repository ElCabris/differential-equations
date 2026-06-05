from __future__ import annotations

import numpy as np
from fastapi import APIRouter
from app.schemas.requests import (
    AnalyticRequest,
    CompareRequest,
    CompareResponse,
    FDMRequest,
    MethodMetrics,
    PINNRequest,
)
from app.services import analytic_service, fdm_service, pinn_service

router = APIRouter(tags=["compare"])


@router.post("/compare", response_model=CompareResponse)
def compare(req: CompareRequest) -> CompareResponse:
    """Run analytic, FTCS and PINN solvers; return solutions + error metrics."""
    params = dict(alpha=req.alpha, L=req.L, T=req.T, Nx=req.Nx, Nt=req.Nt)

    # ── Analytic (reference) ──────────────────────────────────────────────────
    analytic_resp, analytic_time = analytic_service.solve(AnalyticRequest(**params))
    u_ref = np.array(analytic_resp.u)  # (Nt, Nx)

    # ── FTCS ─────────────────────────────────────────────────────────────────
    fdm_resp, fdm_time = fdm_service.solve(FDMRequest(**params))
    u_fdm = np.array(fdm_resp.u)

    # ── PINN ─────────────────────────────────────────────────────────────────
    pinn_resp = None
    try:
        pinn_req = PINNRequest(
            **params,
            load_pretrained=req.pinn_load_pretrained,
            train=req.pinn_train,
            epochs=req.pinn_epochs,
            lr=req.pinn_lr,
            use_lbfgs=req.pinn_use_lbfgs,
        )
        pinn_resp = pinn_service.solve(pinn_req)
    except ValueError:
        pass  # PINN unavailable; omit from comparison

    # ── Error metrics ─────────────────────────────────────────────────────────
    metrics: dict[str, MethodMetrics] = {
        "fdm": _metrics(u_ref, u_fdm, fdm_time),
    }
    if pinn_resp is not None:
        metrics["pinn"] = _metrics(
            u_ref, np.array(pinn_resp.u), pinn_resp.training_time
        )

    return CompareResponse(
        analytic=analytic_resp,
        fdm=fdm_resp,
        pinn=pinn_resp,
        metrics=metrics,
    )


# ── Helpers ───────────────────────────────────────────────────────────────────

def _metrics(u_ref: np.ndarray, u_approx: np.ndarray, elapsed: float) -> MethodMetrics:
    diff = u_ref - u_approx
    l2 = float(np.sqrt(np.mean(diff ** 2)))
    linf = float(np.max(np.abs(diff)))
    return MethodMetrics(l2_error=l2, linf_error=linf, execution_time=elapsed)
