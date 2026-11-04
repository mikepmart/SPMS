# Project: Simulated Patient Monitoring System (SPMS)
# Project Author: Michael Mart | Prepared by Codex
# File: tests/unit/test_bootstrap.py
# Purpose: Specify the isolated, nonclinical ASGI bootstrap before implementation.
# Responsibilities: Factory isolation and disabled debug/documentation defaults.
# Requirements: AR-003, QA-001, QA-002, SEC-013.
# Control: RC-CYB-006 (bootstrap contribution only).
from importlib import import_module

import pytest
from fastapi import FastAPI


@pytest.mark.unit
def test_factory_creates_independent_applications() -> None:
    """Import inside the test so RED identifies missing project behavior."""
    factory = import_module("spms.api.app").create_app
    first = factory()
    second = factory()
    assert isinstance(first, FastAPI)
    assert first is not second


@pytest.mark.security
def test_bootstrap_disables_debug_and_interactive_api_docs() -> None:
    """No remote monitoring API is introduced by the Phase 1 scaffold."""
    app = import_module("spms.api.app").create_app()
    assert app.debug is False
    assert app.docs_url is None
    assert app.redoc_url is None
    assert app.openapi_url is None
