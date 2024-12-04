from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Define a type variable that can be any subclass of Attribute and INameMapIdContract
T = TypeVar('T', bound='INameMapIdContract')

class INameMapIdContract(ABC):
    @property
    @abstractmethod
    def property_name(self) -> str:
        pass

class INameMapIdOf(Generic[T], ABC):
    """A generic interface that requires T to be a subclass of INameMapIdContract."""
    pass