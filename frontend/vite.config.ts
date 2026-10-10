// Project: SPMS | Project Author: Michael Mart | Prepared by Codex
// File: vite.config.ts
// Purpose: Configure a loopback-only frontend and deterministic unit-test setup.
// Responsibilities: React build, strict local ports, unit/coverage evidence.
// Requirements: AR-004, AR-006, QA-004, QA-006, SEC-013, CL-007.
// Control: RC-CYB-006 (supporting development defaults).
import react from "@vitejs/plugin-react";
import { defineConfig } from "vitest/config";

export default defineConfig({
  plugins: [react()],
  server: { host: "127.0.0.1", port: 5173, strictPort: true },
  preview: { host: "127.0.0.1", port: 4173, strictPort: true },
  test: {
    environment: "jsdom",
    setupFiles: ["./src/test/setup.ts"],
    include: ["src/**/*.test.{ts,tsx}"],
    reporters: ["default", "junit"],
    outputFile: { junit: "../artifacts/frontend/unit-junit.xml" },
    coverage: {
      provider: "v8",
      include: ["src/**/*.{ts,tsx}"],
      exclude: ["src/**/*.test.{ts,tsx}", "src/test/**", "src/**/*.d.ts"],
      reporter: ["text", "json-summary", "lcov"],
      reportsDirectory: "../artifacts/frontend/coverage",
    },
  },
});
