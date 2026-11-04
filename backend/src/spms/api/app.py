# Project: Simulated Patient Monitoring System (SPMS)
# Project Author: Michael Mart | Prepared by Codex
# File: api/app.py
# Purpose: Supply an isolated HTTP bootstrap for development smoke verification.
# Responsibilities: Health identity and safe debug/documentation defaults only.
# Requirements: AR-004, QA-003, SEC-013 (supporting scaffold, not full verification).
# Controls: RC-CYB-006 (supporting development defaults).
from fastapi import FastAPI


def create_app() -> FastAPI:
    """Construct a fresh educational scaffold without monitoring state or routes."""
    app = FastAPI(
        title="SPMS Simulation",
        description="Synthetic-data-only educational simulation scaffold.",
        debug=False,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

    @app.get("/health")
    def health() -> dict[str, str | bool]:
        """Identify process availability, not patient or monitoring status."""
        return {"status": "ok", "simulation_only": True}

    return app
