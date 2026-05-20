import pytest
from agents.base import SecurityFinding, Severity


def test_security_finding_creation():
    finding = SecurityFinding(
        agent="sast",
        severity=Severity.HIGH,
        finding="Test finding",
        file="test.py",
        line=10
    )

    assert finding.agent == "sast"
    assert finding.severity == Severity.HIGH
    assert finding.finding == "Test finding"
    assert finding.file == "test.py"
    assert finding.line == 10
    assert finding.finding_id is not None


def test_security_finding_to_dict():
    finding = SecurityFinding(
        agent="sca",
        severity=Severity.CRITICAL,
        finding="Vulnerable dependency",
        cve_id="CVE-2023-1234",
        rule_id="PY-2023-1234",
        remediation="Upgrade package"
    )

    result = finding.to_dict()

    assert result["agent"] == "sca"
    assert result["severity"] == "CRITICAL"
    assert result["cve_id"] == "CVE-2023-1234"
    assert result["metadata"] == {}


def test_severity_enum_values():
    assert Severity.CRITICAL.value == "CRITICAL"
    assert Severity.HIGH.value == "HIGH"
    assert Severity.MEDIUM.value == "MEDIUM"
    assert Severity.LOW.value == "LOW"
    assert Severity.INFO.value == "INFO"
