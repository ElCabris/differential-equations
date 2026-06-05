"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import analytic, fdm, pinn, compare

app = FastAPI(
    title="Heat Equation Solver",
    description="Compare analytic, FTCS and PINN solutions for the 1-D heat equation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytic.router)
app.include_router(fdm.router)
app.include_router(pinn.router)
app.include_router(compare.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
