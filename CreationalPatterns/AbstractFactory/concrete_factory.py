from abstract_factory import ToyAnimalFactory
from concrete_products import Eagle, Lion, Shark


class AquaticAnimalFactory(ToyAnimalFactory):
    def create_toy_animal(self):
        return Shark()


class TerrestrialAnimalFactory(ToyAnimalFactory):
    def create_toy_animal(self):
        return Lion()


class AvianAnimalFactory(ToyAnimalFactory):
    def create_toy_animal(self):
        return Eagle()
