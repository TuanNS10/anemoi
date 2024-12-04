from typing import Union
import asyncio

class NoneType:
    pass

class IUnitOfWork:
    async def save_changes_async(self, token: asyncio.Task = None) -> Union[NoneType, Exception]:
       pass
