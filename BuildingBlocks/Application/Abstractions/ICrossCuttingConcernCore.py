from abc import ABC, abstractmethod

class ICrossCuttingConcernCore(ABC):
    @property
    @abstractmethod
    def property_name(self) -> str:
        pass

    @property
    @abstractmethod
    def expression(self) -> str:
        pass

    @expression.setter
    @abstractmethod
    def expression(self, value: str):
        pass

    @property
    @abstractmethod
    def order(self) -> int:
        pass

    @order.setter
    @abstractmethod
    def order(self, value: int):
        pass

class IDataMappableCore(ICrossCuttingConcernCore):
    pass

class IDataCountingCore(ICrossCuttingConcernCore):
    pass