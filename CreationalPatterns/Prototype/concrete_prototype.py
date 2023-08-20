from prototype import Prototype


class ConcretePrototype(Prototype):
    """
    Concrete implementation of the Prototype interface.
    Contains methods to set and get attributes and to clone the object.
    """

    def __init__(self, attribute1, attribute2):
        """
        Initialize the ConcretePrototype with given attributes.

        Parameters:
        - attribute1: Any type
        - attribute2: Any type
        """
        self._attribute1 = attribute1
        self._attribute2 = attribute2

    def clone(self):
        """
        Create and return a clone of the current object.

        Returns:
        - ConcretePrototype object
        """
        return ConcretePrototype(self._attribute1, self._attribute2)

    def __str__(self):
        return f"ConcretePrototype(attribute1={self._attribute1}, attribute2={self._attribute2})"
