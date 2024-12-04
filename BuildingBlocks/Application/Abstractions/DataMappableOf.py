from typing import List, TypeVar, Generic
from uuid import UUID

from BuildingBlocks.Application.Abstractions.ICrossCuttingConcernCore import IDataMappableCore
from BuildingBlocks.Application.Abstractions.IDataMappableOf import IDataMappableOf

TAttribute = TypeVar('TAttribute', bound='IDataMappableCore')

class GetDataMappableQuery:
    def __init__(self, selector_ids: List[UUID], expression: str):
        self.selector_ids = selector_ids
        self.expression = expression

class DataMappableOf(GetDataMappableQuery, IDataMappableOf[TAttribute]):
    def __init__(self, selector_ids: List[UUID], expression: str):
        super().__init__(selector_ids, expression)
