import json
import os
from dataclasses import dataclass
from typing import Optional

from agents.base import SecurityFinding
from agents.dummy import run_dummy_sast, run_dummy_sca, run_dummy_iac
from pipeline.verdict import compute_verdict
from pipeline.aggregate import generate_sarif


@dataclass
class PipelineContext:
    repo_url: str
    commit_sha: str
    github_token: Optional[str] = None
    pr_number: Optional[int] = None


def run_pipeline(ctx: PipelineContext) -> dict:
    findings: list[SecurityFinding] = []

    findings.extend(run_dummy_sast())
    findings.extend(run_dummy_sca())
    findings.extend(run_dummy_iac())

    findings_dicts = [f.to_dict() for f in findings]
    verdict = compute_verdict(findings_dicts)
    sarif = generate_sarif(findings_dicts)

    return {
        "findings": findings_dicts,
        "verdict": verdict,
        "sarif": sarif,
    }


if __name__ == "__main__":
    ctx = PipelineContext(
        repo_url=os.environ.get("GITHUB_REPOSITORY", ""),
        commit_sha=os.environ.get("GITHUB_SHA", ""),
        github_token=os.environ.get("GITHUB_TOKEN"),
        pr_number=int(os.environ.get("PR_NUMBER", 0)) if os.environ.get("PR_NUMBER") else None,
    )

    result = run_pipeline(ctx)
    print(json.dumps(result, indent=2))
