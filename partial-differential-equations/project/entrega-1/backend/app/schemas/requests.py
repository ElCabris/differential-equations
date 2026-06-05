from __future__ import annotations

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class HeatParams(BaseModel):
    alpha: float = Field(default=0.01, gt=0.0, le=1.0, description="Thermal diffusivity")
    L: float = Field(default=1.0, gt=0.0, description="Domain length [m]")
    T: float = Field(default=1.0, gt=0.0, description="Total simulation time [s]")
    Nx: int = Field(default=100, ge=10, le=500, description="Number of spatial grid points")
    Nt: int = Field(default=100, ge=10, le=500, description="Number of temporal grid points")


class AnalyticRequest(HeatParams):
    pass


class FDMRequest(HeatParams):
    pass


class PINNRequest(HeatParams):
    load_pretrained: bool = Field(default=True, description="Load model from saved_models/")
    train: bool = Field(default=False, description="Train a new model")
    epochs: int = Field(default=2000, ge=100, le=10000, description="Adam optimizer epochs")
    lr: float = Field(default=1e-3, gt=0.0, description="Adam learning rate")
    use_lbfgs: bool = Field(default=True, description="Apply LBFGS refinement after Adam")


class CompareRequest(HeatParams):
    pinn_load_pretrained: bool = Field(default=True)
    pinn_train: bool = Field(default=False)
    pinn_epochs: int = Field(default=2000, ge=100, le=10000)
    pinn_lr: float = Field(default=1e-3, gt=0.0)
    pinn_use_lbfgs: bool = Field(default=True)


# --- Responses ---

class SolutionResponse(BaseModel):
    x: List[float]
    t: List[float]
    u: List[List[float]]


class FDMResponse(SolutionResponse):
    fourier_number: float
    stable: bool
    warning: Optional[str] = None


class PINNResponse(SolutionResponse):
    loss_history: List[float]
    training_time: float
    loaded_pretrained: bool


class MethodMetrics(BaseModel):
    l2_error: float
    linf_error: float
    execution_time: float


class CompareResponse(BaseModel):
    analytic: SolutionResponse
    fdm: FDMResponse
    pinn: Optional[PINNResponse] = None
    metrics: Dict[str, MethodMetrics]
