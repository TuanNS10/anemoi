from abc import ABC, abstractmethod

from BuildingBlocks.Application.ApplicationModels.HeaderContext import HeaderContext

class IHeaderContextProvider(ABC):
    @abstractmethod
    def create_context(self) -> HeaderContext:
        pass

    @abstractmethod
    def get_context(self) -> HeaderContext:
        pass