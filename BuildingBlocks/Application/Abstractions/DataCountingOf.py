from typing import List, TypeVar, Generic

from BuildingBlocks.Application.Abstractions.ICrossCuttingConcernCore import IDataCountingCore
from BuildingBlocks.Application.Abstractions.IDataCountingOf import IDataCountingOf

TAttribute = TypeVar('TAttribute', bound='IDataCountingCore')

class GetDataCountingQuery:
    def __init__(self, selectors: List[str], expression: str):
        self.selectors = selectors
        self.expression = expression

class DataCountingOf(GetDataCountingQuery, IDataCountingOf[TAttribute]):
    def __init__(self, selectors: List[str], expression: str):
        super().__init__(selectors, expression)
