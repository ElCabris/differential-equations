"""PINN architecture extracted verbatim from entrega-1.ipynb.

MLP: (x, t) → [2→32 tanh → 32 tanh → 32 tanh → 1]
"""

from __future__ import annotations

import torch
import torch.nn as nn


class PINN(nn.Module):
    """Physics-Informed Neural Network for the 1D heat equation.

    Identical to the architecture defined in entrega-1.ipynb:
        Input  : (x, t)             — 2 features
        Hidden : 32 → 32 → 32      — tanh activations
        Output : û(x, t)            — scalar temperature
    """

    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 32), nn.Tanh(),
            nn.Linear(32, 32), nn.Tanh(),
            nn.Linear(32, 32), nn.Tanh(),
            nn.Linear(32, 1),
        )

    def forward(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Predict temperature.

        Args:
            x: Spatial coords,  shape (N, 1).
            t: Time coords,     shape (N, 1).

        Returns:
            û: Temperature,     shape (N, 1).
        """
        return self.net(torch.cat([x, t], dim=1))
