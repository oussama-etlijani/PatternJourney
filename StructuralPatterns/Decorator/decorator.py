from abc import ABC, abstractmethod


# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0  # Base cost for a simple coffee


# Decorator
class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self) -> float:
        pass


# Concrete Decorators
class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5


class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0


class FlavorDecorator(CoffeeDecorator):
    def __init__(self, coffee: Coffee, flavor: str):
        super().__init__(coffee)
        self._flavor = flavor

    def cost(self) -> float:
        return self._coffee.cost() + 1.5

    def __str__(self) -> str:
        return f"{self._flavor} {self._coffee}"


def client_code(coffee: Coffee) -> None:
    print(f"Cost of {coffee}: ${coffee.cost()}")


if __name__ == "__main__":
    # Create a simple coffee
    simple_coffee = SimpleCoffee()
    client_code(simple_coffee)
    print("\n")

    # Decorate the simple coffee with sugar
    sugar_coffee = SugarDecorator(simple_coffee)
    client_code(sugar_coffee)
    print("\n")

    # Decorate the sugar coffee with milk
    sugar_milk_coffee = MilkDecorator(sugar_coffee)
    client_code(sugar_milk_coffee)
    print("\n")

    # Decorate the sugar milk coffee with a flavor
    flavored_coffee = FlavorDecorator(sugar_milk_coffee, "Vanilla")
    client_code(flavored_coffee)
