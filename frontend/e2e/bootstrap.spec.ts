// Project: Simulated Patient Monitoring System (SPMS)
// Project Author: Michael Mart | Prepared by Codex
// File: e2e/bootstrap.spec.ts
// Purpose: Verify the built UI and installed backend through real local servers.
// Responsibilities: Chromium rendering, exact warning, HTTP health and runtime errors.
// Requirements: QA-003, QA-004, QA-008, SF-001, PRIV-001.
// Control: RC-SAF-010 (scaffold contribution only).
import { expect, test } from "@playwright/test";

test("loads the stopped simulation shell and the nonclinical backend", async ({
  page,
  request,
}) => {
  const runtimeErrors: string[] = [];
  page.on("pageerror", (error) => runtimeErrors.push(error.message));
  await page.goto("/");
  await expect(
    page.getByRole("heading", { name: "SPMS Simulation", level: 1 }),
  ).toBeVisible();
  await expect(
    page.getByText("Simulation only — not for clinical use."),
  ).toBeVisible();
  await expect(page.getByText("Simulation is not running.")).toBeVisible();
  const health = await request.get("http://127.0.0.1:8000/health");
  expect(health.ok()).toBe(true);
  expect(await health.json()).toEqual({ status: "ok", simulation_only: true });
  expect(runtimeErrors).toEqual([]);
});
