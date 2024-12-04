from abc import ABC, abstractmethod
import asyncio
from typing import List, Dict, Union, Optional

from BuildingBlocks.Application.ApplicationModels.FileData import FileData
from BuildingBlocks.Application.ApplicationModels.FileResponseData import FileResponseData

class IFileService(ABC):
    @abstractmethod
    async def save_files_async(self, files: List[FileData], folder_name: str, token: asyncio.Event = None) -> Union[List[str], Exception]:
        pass

    @abstractmethod
    async def save_stream_file_async(self, stream, folder_name: str, file_name: str, metadata: Dict[str, str], token: asyncio.Event = None) -> Union[str, Exception]:
        pass

    @abstractmethod
    async def copy_file_async(self, source_key: str, destination_key: str, token: asyncio.Event = None) -> Union[str, Exception]:
        pass

    @abstractmethod
    async def get_file_async(self, key: str, token: asyncio.Event = None) -> Union[FileResponseData, Exception]:
        pass

    @abstractmethod
    async def get_file_metadata_async(self, key: str, header_key: str, token: asyncio.Event = None) -> Union[str, Exception]:
        pass

    @abstractmethod
    async def get_file_size_async(self, key: str, token: asyncio.Event = None) -> int:
        pass

    @abstractmethod
    async def remove_folder_async(self, folder: str, token: asyncio.Event = None):
        pass

    @abstractmethod
    async def save_file_base64_async(self, base64_string: str, folder_name: str, token: asyncio.Event = None) -> Union[str, Exception]:
        pass

    @abstractmethod
    async def generate_pre_signed_url_async(self, key: str, prefer_bucket: str, token: asyncio.Event = None) -> Union[str, Exception]:
        pass
