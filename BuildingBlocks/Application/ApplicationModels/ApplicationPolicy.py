from dataclasses import dataclass

@dataclass(frozen=True)
class ApplicationPolicy:
    key: str
    value: str
    