from abc import ABC, abstractmethod

from BuildingBlocks.Application.ApplicationModels.ApplicationPolicy import ApplicationPolicy

class IApplicationPolicyGetter(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        pass

    @property
    @abstractmethod
    def value(self) -> str:
        pass


class IApplicationPolicySetter(ABC):
    @abstractmethod
    def set_application_policy(self, application_policy: ApplicationPolicy):
        pass
    