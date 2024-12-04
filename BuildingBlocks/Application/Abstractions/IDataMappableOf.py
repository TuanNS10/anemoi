from abc import ABC, abstractmethod

from BuildingBlocks.Application.Abstractions.ICrossCuttingConcernCore import IDataMappableCore

class IDataMappableOf(ABC):
    @abstractmethod
    def get_generic_argument_type(self) -> IDataMappableCore:
        pass