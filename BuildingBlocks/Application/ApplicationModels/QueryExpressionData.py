from dataclasses import dataclass
from typing import Type

@dataclass(frozen=True)
class QueryExpressionData:
    expression: str
    model_type: Type
    