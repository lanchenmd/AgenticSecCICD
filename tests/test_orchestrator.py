import pytest
from pipeline.verdict import compute_verdict, BLOCK_THRESHOLD, WARN_THRESHOLD
from agents.base import Severity


def test_compute_verdict_empty():
    assert compute_verdict([]) == "PASS"


def test_compute_verdict_info_only():
    findings = [{"severity": "INFO", "finding": "test"}]
    assert compute_verdict(findings) == "PASS"


def test_compute_verdict_low():
    findings = [{"severity": "LOW", "finding": "test"}]
    assert compute_verdict(findings) == "PASS"


def test_compute_verdict_medium():
    findings = [{"severity": "MEDIUM", "finding": "test"}]
    assert compute_verdict(findings) == "WARN"


def test_compute_verdict_high():
    findings = [{"severity": "HIGH", "finding": "test"}]
    assert compute_verdict(findings) == "BLOCK"


def test_compute_verdict_critical():
    findings = [{"severity": "CRITICAL", "finding": "test"}]
    assert compute_verdict(findings) == "BLOCK"


def test_compute_verdict_multiple_findings_takes_worst():
    findings = [
        {"severity": "INFO", "finding": "test1"},
        {"severity": "MEDIUM", "finding": "test2"},
        {"severity": "LOW", "finding": "test3"},
    ]
    assert compute_verdict(findings) == "WARN"


def test_compute_verdict_mixed_critical_and_medium():
    findings = [
        {"severity": "MEDIUM", "finding": "test1"},
        {"severity": "CRITICAL", "finding": "test2"},
    ]
    assert compute_verdict(findings) == "BLOCK"
