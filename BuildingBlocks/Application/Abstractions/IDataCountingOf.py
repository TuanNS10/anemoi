from abc import ABC, abstractmethod

from BuildingBlocks.Application.Abstractions.ICrossCuttingConcernCore import IDataCountingCore

class IDataCountingOf(ABC):
    """Đây là lớp trừu tượng mô phỏng generic interface."""
    
    @abstractmethod
    def get_generic_argument_type(self) -> IDataCountingCore:
        pass