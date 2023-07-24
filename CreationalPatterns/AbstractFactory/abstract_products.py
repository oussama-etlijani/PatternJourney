from abc import ABC, abstractmethod


class ToyAnimal(ABC):
    @abstractmethod
    def interact(self):
        pass


class AquaticAnimal(ToyAnimal):
    pass


class TerrestrialAnimal(ToyAnimal):
    pass


class AvianAnimal(ToyAnimal):
    pass
