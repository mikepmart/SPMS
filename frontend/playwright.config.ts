// Project: SPMS | Project Author: Michael Mart | Prepared by Codex
// File: playwright.config.ts
// Purpose: Verify the built UI and real backend over local HTTP in Chromium.
// Responsibilities: Isolated test servers, reproducible failures and CI reports.
// Requirements: QA-003, QA-004, QA-008, SEC-013, CL-007.
// Control: RC-CYB-006 (supporting loopback-only test configuration).
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  forbidOnly: Boolean(process.env.CI),
  retries: 0,
  workers: 1,
  reporter: [
    ["list"],
    ["junit", { outputFile: "../artifacts/browser/junit.xml" }],
    ["html", { outputFolder: "../artifacts/browser/report", open: "never" }],
  ],
  outputDir: "../artifacts/browser/results",
  use: { baseURL: "http://127.0.0.1:4173", trace: "retain-on-failure" },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
  webServer: [
    {
      command: "npm run preview",
      url: "http://127.0.0.1:4173",
      reuseExistingServer: false,
      timeout: 30_000,
    },
    {
      command:
        "uv run --locked --project ../backend uvicorn spms.api.app:create_app --factory --host 127.0.0.1 --port 8000",
      url: "http://127.0.0.1:8000/health",
      reuseExistingServer: false,
      timeout: 30_000,
    },
  ],
});
