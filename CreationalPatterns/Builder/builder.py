from abc import ABC, abstractmethod


class Builder(ABC):
    """Abstract Builder interface that declares product construction steps"""

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def install_engine(self):
        pass

    @abstractmethod
    def paint_vehicle(self):
        pass

    @abstractmethod
    def get_vehicle(self):
        pass


class ConcreteBuilder1(Builder):
    """Concrete builder class to construct Car objects"""

    def __init__(self):
        self.reset()

    def reset(self):
        self._vehicle = Vehicle()

    def build_body(self):
        self._vehicle.add("Basic body")

    def install_engine(self):
        self._vehicle.add("Basic engine")

    def paint_vehicle(self):
        self._vehicle.add("Standard paint")

    def get_vehicle(self):
        vehicle = self._vehicle
        self.reset()
        return vehicle


class Vehicle:
    """Product"""

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return self.parts
