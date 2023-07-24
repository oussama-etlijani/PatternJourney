from abstract_products import AquaticAnimal, TerrestrialAnimal, AvianAnimal


class Shark(AquaticAnimal):
    def interact(self):
        return "The shark swims around."


class Lion(TerrestrialAnimal):
    def interact(self):
        return "The lion roars."


class Eagle(AvianAnimal):
    def interact(self):
        return "The eagle soars high."
