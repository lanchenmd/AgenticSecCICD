# CLAUDE.md

This is an agentic security CI/CD pipeline project. It uses Python with sequential execution (no LangGraph yet — introduced in Phase 5 for LLM triage).

## Project Overview

Multi-agent security scanning pipeline: SAST (Semgrep), SCA (OSV/pip-audit), IaC (Checkov), with cross-agent triage using Claude API.

## Key Files

- `agents/base.py` — `SecurityFinding` dataclass + `Severity` enum
- `agents/dummy.py` — Phase 1 stub agents with simulated findings
- `pipeline/orchestrator.py` — Sequential pipeline runner
- `pipeline/verdict.py` — BLOCK/WARN/PASS verdict logic
- `pipeline/aggregate.py` — SARIF generation
- `.github/workflows/security-pipeline.yml` — Matrix jobs (sast/sca/iac parallel)

## Design Decisions

- Sequential execution in Phase 1; LangGraph added in Phase 5
- Matrix jobs in GitHub Actions (parallel agent execution)
- SARIF output after all agents complete (not real-time)
- YAML config files for agent settings

## GitHub Repo

https://github.com/lanchenmd/AgenticSecCICD

## Running Tests

```bash
pytest tests/ -v
```

## Workflow

```bash
git add . && git commit -m "message" && git push
```
