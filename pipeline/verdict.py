from agents.base import Severity
from typing import List

BLOCK_THRESHOLD = Severity.HIGH
WARN_THRESHOLD = Severity.MEDIUM

SEVERITY_RANK = {
    Severity.CRITICAL: 1,
    Severity.HIGH: 2,
    Severity.MEDIUM: 3,
    Severity.LOW: 4,
    Severity.INFO: 5,
}


def compute_verdict(findings: List[dict]) -> str:
    if not findings:
        return "PASS"

    max_severity = min(
        (Severity(f["severity"]) for f in findings),
        key=lambda s: SEVERITY_RANK[s]
    )

    if SEVERITY_RANK[max_severity] <= SEVERITY_RANK[BLOCK_THRESHOLD]:
        return "BLOCK"
    elif SEVERITY_RANK[max_severity] <= SEVERITY_RANK[WARN_THRESHOLD]:
        return "WARN"
    else:
        return "PASS"
