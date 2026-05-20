import json
import sys
from typing import List, Any
from datetime import datetime, timezone


def generate_sarif(findings: List[dict]) -> dict:
    rules = {}
    results = []

    for i, finding in enumerate(findings):
        rule_id = finding.get("rule_id") or f"rule-{i}"
        if rule_id not in rules:
            rules[rule_id] = {
                "id": rule_id,
                "name": finding.get("agent", "unknown"),
                "shortDescription": {
                    "text": finding.get("finding", "")
                },
                "properties": {
                    "severity": finding.get("severity", "UNKNOWN")
                }
            }

        result = {
            "ruleId": rule_id,
            "level": severity_to_sarif_level(finding.get("severity", "INFO")),
            "message": {
                "text": finding.get("finding", "")
            },
            "locations": []
        }

        if finding.get("file"):
            result["locations"].append({
                "physicalLocation": {
                    "artifactLocation": {
                        "uri": finding.get("file", "")
                    },
                    "region": {
                        "startLine": finding.get("line", 1)
                    }
                }
            })

        results.append(result)

    return {
        "version": "2.1.0",
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "AgenticSecCICD",
                    "version": "1.0.0",
                    "rules": list(rules.values())
                }
            },
            "results": results,
            "properties": {
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }]
    }


def severity_to_sarif_level(severity: str) -> str:
    mapping = {
        "CRITICAL": "error",
        "HIGH": "error",
        "MEDIUM": "warning",
        "LOW": "note",
        "INFO": "note"
    }
    return mapping.get(severity, "note")


if __name__ == "__main__":
    all_findings = []

    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                findings = json.loads(line)
                if isinstance(findings, list):
                    all_findings.extend(findings)
            except json.JSONDecodeError:
                pass

    sarif = generate_sarif(all_findings)
    with open("results.sarif", "w") as f:
        json.dump(sarif, f, indent=2)
