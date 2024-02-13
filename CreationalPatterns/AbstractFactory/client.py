from concrete_factory import TerrestrialAnimalFactory


class ToyShop:
    # The ToyShop class initializes with a factory object.
    def __init__(self, factory):
        # The factory object is stored as an instance variable.
        self.factory = factory

    # The order_toy_animal method creates a toy animal using the factory object.
    def order_toy_animal(self):
        # The factory object's create_toy_animal method is called to create the toy.
        toy = self.factory.create_toy_animal()
        # The toy's interact method is called to simulate interaction with the toy.
        result = toy.interact()
        # The result of the interaction is returned.
        return result


# The client code starts execution here.
if __name__ == "__main__":
    # An instance of the TerrestrialAnimalFactory is created.
    factory = TerrestrialAnimalFactory()
    # A ToyShop object is created with the factory object as an argument.
    shop = ToyShop(factory)
    # The order_toy_animal method of the ToyShop object is called.
    # The returned result is printed to the console.
    print(shop.order_toy_animal())  # Outputs: "The lion roars."
