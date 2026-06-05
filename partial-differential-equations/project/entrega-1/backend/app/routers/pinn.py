from fastapi import APIRouter, HTTPException
from app.schemas.requests import PINNRequest, PINNResponse
from app.services import pinn_service

router = APIRouter(prefix="/solve", tags=["pinn"])


@router.post("/pinn", response_model=PINNResponse)
def solve_pinn(req: PINNRequest) -> PINNResponse:
    """Solve via PINN.  Loads a pretrained model or trains from scratch."""
    try:
        return pinn_service.solve(req)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
