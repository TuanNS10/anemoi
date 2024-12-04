from typing import Callable, List, Union, Optional
from sqlalchemy.orm import Query
from sqlalchemy import text
import asyncio

class NoneType:
    pass

class Pagination:
    def __init__(self, items: List, total_count: int):
        self.items = items
        self.total_count = total_count

class ISqlRepository:
    def get_queryable(self, condition_expression: Optional[Callable] = None) -> Query:
        raise NotImplementedError
    
    def get_queryable_from_raw_query(self, sql: str, *parameters) -> Query:
        raise NotImplementedError
    
    async def get_first_by_condition_async(self, condition_expression: Optional[Callable] = None,
                                           special_action: Optional[Callable] = None, 
                                           token: Optional[asyncio.Task] = None) -> Optional[object]:
        raise NotImplementedError
    
    async def exist_by_condition_async(self, condition_expression: Optional[Callable] = None, 
                                       token: Optional[asyncio.Task] = None) -> bool:
        raise NotImplementedError
    
    async def get_many_by_condition_async(self, condition_expression: Optional[Callable] = None,
                                          special_action: Optional[Callable] = None, 
                                          token: Optional[asyncio.Task] = None) -> List[object]:
        raise NotImplementedError
    
    async def get_many_by_condition_with_pagination_async(self, condition_expression: Optional[Callable] = None,
                                                          special_action: Optional[Callable] = None, 
                                                          token: Optional[asyncio.Task] = None) -> Pagination:
        raise NotImplementedError
    
    async def count_by_condition_async(self, condition_expression: Optional[Callable] = None, 
                                       special_action: Optional[Callable] = None, 
                                       token: Optional[asyncio.Task] = None) -> int:
        raise NotImplementedError
    
    async def create_one_async(self, item: object, token: Optional[asyncio.Task] = None) -> Union[object, Exception]:
        raise NotImplementedError
    
    async def create_many_async(self, items: List[object], token: Optional[asyncio.Task] = None) -> Union[NoneType, Exception]:
        raise NotImplementedError
    
    async def remove_one_async(self, item_or_filter: Union[object, Callable], 
                               token: Optional[asyncio.Task] = None) -> Union[NoneType, Exception]:
        raise NotImplementedError
    
    async def remove_many_async(self, items_or_filter: Union[List[object], Callable], 
                                token: Optional[asyncio.Task] = None) -> Union[NoneType, Exception]:
        raise NotImplementedError
