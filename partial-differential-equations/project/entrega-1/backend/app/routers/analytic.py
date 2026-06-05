from fastapi import APIRouter
from app.schemas.requests import AnalyticRequest, SolutionResponse
from app.services import analytic_service

router = APIRouter(prefix="/solve", tags=["analytic"])


@router.post("/analytic", response_model=SolutionResponse)
def solve_analytic(req: AnalyticRequest) -> SolutionResponse:
    """Compute the exact analytic solution of the 1-D heat equation."""
    response, _ = analytic_service.solve(req)
    return response
