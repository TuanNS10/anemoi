from abc import ABC, abstractmethod

class ITokenGetter(ABC):
    @property
    @abstractmethod
    def token(self) -> str:
        pass

class ITokenSetter(ABC):
    @abstractmethod
    def set_token(self, token: str) -> None:
        pass