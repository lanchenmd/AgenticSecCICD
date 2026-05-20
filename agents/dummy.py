import argparse
from typing import List
from agents.base import SecurityFinding, Severity


def run_dummy_sast() -> List[SecurityFinding]:
    return [
        SecurityFinding(
            agent="sast",
            severity=Severity.MEDIUM,
            finding="Potential SQL injection in user input",
            file="src/api.py",
            line=42,
            rule_id="python.sql.injection",
            remediation="Use parameterized queries"
        )
    ]


def run_dummy_sca() -> List[SecurityFinding]:
    return [
        SecurityFinding(
            agent="sca",
            severity=Severity.HIGH,
            finding="Vulnerable dependency: requests 2.26.0",
            cve_id="CVE-2023-32681",
            rule_id="PY-2023-32681",
            remediation="Upgrade to requests>=2.31.0"
        )
    ]


def run_dummy_iac() -> List[SecurityFinding]:
    return [
        SecurityFinding(
            agent="iac",
            severity=Severity.CRITICAL,
            finding="S3 bucket is publicly accessible",
            file="terraform/main.tf",
            line=15,
            rule_id="CKV_AWS_144",
            remediation="Enable public_access_block on the S3 bucket"
        )
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", required=True, choices=["sast", "sca", "iac"])
    args = parser.parse_args()

    if args.agent == "sast":
        findings = run_dummy_sast()
    elif args.agent == "sca":
        findings = run_dummy_sca()
    else:
        findings = run_dummy_iac()

    import json
    import sys
    json.dump([f.to_dict() for f in findings], sys.stdout, indent=2)
