from abc import ABC, abstractmethod

class ISubstituteIdAutoIncrement(ABC):
    @property
    @abstractmethod
    def substitute_id(self) -> int:
        pass

    @substitute_id.setter
    @abstractmethod
    def substitute_id(self, value: int) -> None:
        pass
    