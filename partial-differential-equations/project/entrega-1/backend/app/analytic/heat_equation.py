"""Analytic solution for the 1D heat equation.

PDE:  ∂u/∂t = α ∂²u/∂x²,  x ∈ [0, L],  t ∈ [0, T]
IC:   u(x, 0) = sin(πx/L)
BC:   u(0, t) = u(L, t) = 0

Exact solution (extracted from entrega-1.ipynb):
    u*(x, t) = exp(-α (π/L)² t) · sin(πx/L)
"""

from __future__ import annotations

import numpy as np


def solve(
    alpha: float,
    L: float,
    T: float,
    Nx: int,
    Nt: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute the analytic solution on a uniform grid.

    Args:
        alpha: Thermal diffusivity.
        L:     Domain length.
        T:     Total time.
        Nx:    Number of spatial points.
        Nt:    Number of temporal points.

    Returns:
        x:  Spatial coordinates, shape (Nx,).
        t:  Time coordinates,    shape (Nt,).
        u:  Temperature field,   shape (Nt, Nx).
    """
    x = np.linspace(0.0, L, Nx)
    t = np.linspace(0.0, T, Nt)
    X, T_grid = np.meshgrid(x, t)  # shapes (Nt, Nx)

    # u*(x,t) = exp(-α (π/L)² t) · sin(πx/L)  (from entrega-1.ipynb)
    u = np.exp(-alpha * (np.pi / L) ** 2 * T_grid) * np.sin(np.pi * X / L)

    return x, t, u
