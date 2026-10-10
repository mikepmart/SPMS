# Project: Simulated Patient Monitoring System (SPMS)
# Project Author: Michael Mart | Prepared by Codex
# File: tests/integration/test_health.py
# Purpose: Specify a real ASGI health request for reproducible backend setup.
# Responsibilities: HTTP smoke and absence of undocumented monitoring endpoints.
# Requirements: QA-001, QA-003, SEC-013; no monitoring requirement verified.
# Control: RC-CYB-006 (bootstrap contribution only).
from importlib import import_module

import pytest
from fastapi.testclient import TestClient


@pytest.mark.integration
def test_health_identifies_the_synthetic_only_scaffold() -> None:
    """Successful package installation must also produce a working ASGI app."""
    with TestClient(import_module("spms.api.app").create_app()) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "simulation_only": True}


@pytest.mark.integration
def test_monitoring_routes_are_not_exposed_by_bootstrap() -> None:
    """Phase 1 must not accidentally enable unimplemented monitoring operations."""
    with TestClient(import_module("spms.api.app").create_app()) as client:
        response = client.post("/api/v1/sessions", json={})
    assert response.status_code == 404
