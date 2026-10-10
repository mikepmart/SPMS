// Project: Simulated Patient Monitoring System (SPMS)
// Project Author: Michael Mart | Prepared by Codex
// File: App.test.tsx
// Purpose: Define the accessible, stopped simulation shell before implementation.
// Responsibilities: Visible exact warning and honest absence of live monitoring.
// Requirements: QA-001, QA-004, SF-001, PRIV-001.
// Control: RC-SAF-010 (scaffold contribution; full screen coverage is later work).
import { render, screen } from "@testing-library/react";
import { expect, test } from "vitest";

test("identifies a stopped synthetic simulation with the exact nonclinical notice", async () => {
  const { default: App } = await import("./App");
  render(<App />);
  expect(
    screen.getByRole("heading", { name: "SPMS Simulation", level: 1 }),
  ).toBeVisible();
  expect(
    screen.getByText("Simulation only — not for clinical use."),
  ).toBeVisible();
  expect(screen.getByText("Simulation is not running.")).toBeVisible();
  expect(screen.getByText("Synthetic data only.")).toBeVisible();
});
