// Project: Simulated Patient Monitoring System (SPMS)
// Project Author: Michael Mart | Prepared by Codex
// File: main.tsx
// Purpose: Mount the development simulation shell.
// Responsibilities: Validate the HTML mount point and initialize React.
// Requirements: AR-004, SF-001; no monitoring risk control implemented here.
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles.css";

const root = document.getElementById("root");
if (!root) throw new Error("SPMS root element is missing");

createRoot(root).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
