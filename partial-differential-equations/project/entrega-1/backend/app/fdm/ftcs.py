"""Explicit FTCS (Forward-Time Centered-Space) finite difference scheme
for the 1D heat equation.

Discretization:
    (u_i^{n+1} - u_i^n) / Δt = α (u_{i+1}^n - 2u_i^n + u_{i-1}^n) / Δx²

    ⟹  u_i^{n+1} = u_i^n + Fo · (u_{i+1}^n - 2u_i^n + u_{i-1}^n)

where Fo = α Δt / Δx²  (mesh Fourier number).

Stability condition:  Fo ≤ 0.5
"""

from __future__ import annotations

import numpy as np


def solve(
    alpha: float,
    L: float,
    T: float,
    Nx: int,
    Nt: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, bool]:
    """Solve the heat equation with the FTCS scheme.

    IC: u(x, 0) = sin(πx/L)
    BC: u(0, t) = u(L, t) = 0

    Args:
        alpha: Thermal diffusivity.
        L:     Domain length.
        T:     Total time.
        Nx:    Number of spatial grid points.
        Nt:    Number of temporal steps.

    Returns:
        x:             Spatial grid, shape (Nx,).
        t:             Time grid,    shape (Nt,).
        u:             Temperature,  shape (Nt, Nx).
        fourier_number: Mesh Fourier number Fo = α·Δt/Δx².
        stable:        True when Fo ≤ 0.5.
    """
    dx = L / (Nx - 1)
    dt = T / (Nt - 1)
    fourier_number = alpha * dt / dx ** 2
    stable = fourier_number <= 0.5

    x = np.linspace(0.0, L, Nx)
    t = np.linspace(0.0, T, Nt)

    u = np.zeros((Nt, Nx))

    # Initial condition: u(x, 0) = sin(πx/L)
    u[0, :] = np.sin(np.pi * x / L)

    # Boundary conditions are zero (already initialised to 0)

    # Time-stepping loop
    fo = fourier_number  # Fo coefficient
    for n in range(Nt - 1):
        u[n + 1, 1:-1] = (
            u[n, 1:-1]
            + fo * (u[n, 2:] - 2.0 * u[n, 1:-1] + u[n, :-2])
        )
        # Dirichlet BCs: u[n+1, 0] = u[n+1, -1] = 0 (already zero)

    return x, t, u, fourier_number, stable
