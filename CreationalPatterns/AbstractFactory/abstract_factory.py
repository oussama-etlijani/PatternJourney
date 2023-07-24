from abc import ABC, abstractmethod


class ToyAnimalFactory(ABC):
    @abstractmethod
    def create_toy_animal(self):
        pass
