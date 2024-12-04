from abc import ABC

class ExcludeFromTopology:
    pass

class IRequestMappable(ABC):
    """An interface that is mappable for requests."""
    # This class can be marked with ExcludeFromTopology if necessary, 
    # but in Python, we typically use comments or documentation instead.