import asyncio
from abc import ABC, abstractmethod

class IDataMappableService(ABC):
    @abstractmethod
    async def map_data_async(self, value: object, token: asyncio.Event = None):
        pass 
