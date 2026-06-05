from __future__ import annotations

import time

from app.fdm import ftcs
from app.schemas.requests import FDMRequest, FDMResponse


def solve(req: FDMRequest) -> tuple[FDMResponse, float]:
    """Run the FTCS solver and return (response, elapsed_seconds)."""
    t0 = time.perf_counter()
    x, t, u, fo, stable = ftcs.solve(req.alpha, req.L, req.T, req.Nx, req.Nt)
    elapsed = time.perf_counter() - t0

    warning = (
        f"Fourier number Fo={fo:.4f} > 0.5 — scheme is unstable."
        if not stable
        else None
    )

    return FDMResponse(
        x=x.tolist(),
        t=t.tolist(),
        u=u.tolist(),
        fourier_number=float(fo),
        stable=stable,
        warning=warning,
    ), elapsed
