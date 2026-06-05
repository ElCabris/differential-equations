from __future__ import annotations

import time

from app.analytic import heat_equation
from app.schemas.requests import AnalyticRequest, SolutionResponse


def solve(req: AnalyticRequest) -> tuple[SolutionResponse, float]:
    """Run the analytic solver and return (response, elapsed_seconds)."""
    t0 = time.perf_counter()
    x, t, u = heat_equation.solve(req.alpha, req.L, req.T, req.Nx, req.Nt)
    elapsed = time.perf_counter() - t0

    return SolutionResponse(
        x=x.tolist(),
        t=t.tolist(),
        u=u.tolist(),
    ), elapsed
