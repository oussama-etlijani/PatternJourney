from abc import ABC, abstractmethod


class Prototype(ABC):
    """
    The abstract base class defining the Prototype interface.
    Contains an abstract method `clone` which concrete classes must implement.
    """

    @abstractmethod
    def clone(self):
        """
        Abstract method for cloning an object.
        """
        pass
