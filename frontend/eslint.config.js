// Project: SPMS | Project Author: Michael Mart | Prepared by Codex
// File: eslint.config.js
// Purpose: Apply React/TypeScript lint rules to maintained frontend code.
// Responsibilities: Zero-warning lint, safe hooks and refresh-compatible modules.
// Requirements: AR-004, AR-005, QA-007.
import js from "@eslint/js";
import { defineConfig, globalIgnores } from "eslint/config";
import tseslint from "typescript-eslint";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";

export default defineConfig([
  globalIgnores([
    "dist/**",
    "coverage/**",
    "playwright-report/**",
    "test-results/**",
  ]),
  js.configs.recommended,
  tseslint.configs.recommended,
  {
    files: ["src/**/*.{ts,tsx}"],
    extends: [reactHooks.configs.flat.recommended, reactRefresh.configs.vite],
  },
]);
