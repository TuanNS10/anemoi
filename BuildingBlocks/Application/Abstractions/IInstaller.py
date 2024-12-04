from abc import ABC, abstractmethod

class IConfiguration:
    pass

class IServiceCollection:
    pass

class IInstaller(ABC):
    @abstractmethod
    def install_services(self, services: IServiceCollection, configuration: IConfiguration):
        pass
    