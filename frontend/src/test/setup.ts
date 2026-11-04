// Project: SPMS | Project Author: Michael Mart | Prepared by Codex
// File: test/setup.ts
// Purpose: Provide DOM assertions and isolate React tests from one another.
// Responsibilities: Matcher registration and automatic rendered-tree cleanup.
// Requirements: QA-004, QA-007.
import "@testing-library/jest-dom/vitest";
import { cleanup } from "@testing-library/react";
import { afterEach } from "vitest";

afterEach(cleanup);
