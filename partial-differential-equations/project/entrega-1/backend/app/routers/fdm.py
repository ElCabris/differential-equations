from fastapi import APIRouter
from app.schemas.requests import FDMRequest, FDMResponse
from app.services import fdm_service

router = APIRouter(prefix="/solve", tags=["fdm"])


@router.post("/fdm", response_model=FDMResponse)
def solve_fdm(req: FDMRequest) -> FDMResponse:
    """Solve the heat equation with the explicit FTCS finite-difference scheme."""
    response, _ = fdm_service.solve(req)
    return response
