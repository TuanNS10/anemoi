from dataclasses import dataclass
from typing import Any, Callable, List, Type

class ICrossCuttingConcernCore:
    pass

@dataclass(frozen=True)
class CrossCuttingDataProperty:
    property_info: Any
    model: Any
    attribute: ICrossCuttingConcernCore
    func: Callable
    expression: str
    order: int

@dataclass(frozen=True)
class CrossCuttingDataPropertyCache:
    attribute: ICrossCuttingConcernCore
    func: Callable
    expression: str
    order: int

@dataclass(frozen=True)
class CrossCuttingTypeData:
    cross_cutting_type: Type
    property_called_laters: List['PropertyCalledLater']
    expression: str
    order: int

@dataclass(frozen=True)
class PropertyCalledLater:
    model: Any
    func: Callable
