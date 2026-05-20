# AgenticSecCICD

Genetic AI for Automated Security in CI/CD Pipelines.

## Overview

This project implements a multi-agent security scanning pipeline that runs in GitHub Actions. It provides SAST, SCA, and IaC scanning with cross-agent triage to detect and report security vulnerabilities in your CI/CD pipeline.

## Phases

| Phase | Component | Description |
|-------|-----------|-------------|
| 1 | Foundation | Project structure, orchestrator, GitHub Actions |
| 2 | SAST | Semgrep-based static analysis |
| 3 | SCA | OSV/pip-audit vulnerability scanning |
| 4 | IaC | Checkov infrastructure scanning |
| 5 | Triage | LLM-powered cross-agent correlation |
| 6 | Quality Gate | SARIF reporting, deployment blocking |

Full phase details are documented in `plan.txt`.

## Project Structure

```
AgenticSecCICD/
├── agents/                    # Security agents
│   ├── base.py               # SecurityFinding schema
│   └── dummy.py              # Phase 1 stub agents
├── pipeline/                  # Orchestration
│   ├── orchestrator.py       # Pipeline runner
│   ├── verdict.py            # BLOCK/WARN/PASS logic
│   ├── aggregate.py          # SARIF generation
│   └── config.py             # Config loader
├── config/                    # YAML configurations
├── tests/                     # Unit tests
└── .github/workflows/         # GitHub Actions
```

## Quick Start

```bash
pip install -r requirements.txt
python -m pipeline.orchestrator
pytest tests/ -v
```

## GitHub Actions

Push to `main` or open a PR to trigger the Security Pipeline. The workflow runs three parallel jobs (SAST, SCA, IaC) and aggregates results into SARIF format.

## Verification (Phase 1)

- 11 unit tests passing
- Dummy agents produce simulated findings
- Verdict correctly returns BLOCK when CRITICAL findings present
- GitHub Actions matrix workflow operational

## Current Status

**Phase 1 Complete** — Foundation and infrastructure scaffolded with dummy agents. Ready for Phase 2 (SAST with Semgrep).
