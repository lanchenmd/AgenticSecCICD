from dataclasses import dataclass, asdict
from typing import Optional
from enum import Enum
import uuid


class Severity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"


@dataclass
class SecurityFinding:
    agent: str
    severity: Severity
    finding: str
    file: Optional[str] = None
    line: Optional[int] = None
    cve_id: Optional[str] = None
    rule_id: Optional[str] = None
    remediation: Optional[str] = None
    metadata: Optional[dict] = None
    finding_id: Optional[str] = None

    def __post_init__(self):
        self.finding_id = self.finding_id or str(uuid.uuid4())[:8]
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> dict:
        result = asdict(self)
        result["severity"] = self.severity.value
        return result
