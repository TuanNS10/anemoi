from abc import ABC, abstractmethod

class IAdministratorGetter(ABC):
    @property
    @abstractmethod
    def is_administrator(self) -> bool:
        pass

class IAdministratorSetter(ABC):
    @abstractmethod
    def set_administrator(self, is_administrator: bool) -> None:
        pass
