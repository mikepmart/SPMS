// Project: Simulated Patient Monitoring System (SPMS)
// Project Author: Michael Mart | Prepared by Codex
// File: App.tsx
// Purpose: Display the initial educational simulation shell.
// Responsibilities: Accessible nonclinical notice and truthful stopped state.
// Requirements: SF-001, PRIV-001 (scaffold contribution only).
// Control: RC-SAF-010 (full future screen verification remains pending).
import type { ReactElement } from "react";

export default function App(): ReactElement {
  return (
    <main className="shell">
      <p className="eyebrow">Educational engineering project</p>
      <h1>SPMS Simulation</h1>
      <p className="notice">Simulation only — not for clinical use.</p>
      <section aria-labelledby="status-heading" className="status">
        <h2 id="status-heading">Simulation status</h2>
        <p>Simulation is not running.</p>
        <p>Synthetic data only.</p>
      </section>
    </main>
  );
}
