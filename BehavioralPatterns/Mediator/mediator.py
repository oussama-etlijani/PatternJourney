from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class ProductItem(BaseComponent):
    def display(self) -> None:
        print("Displaying product details.")


class QuantityInput(BaseComponent):
    def update_quantity(self) -> None:
        print("Updating quantity based on customization.")


class Customization(BaseComponent):
    def select_option(self) -> None:
        print("Customization option selected.")
        self.mediator.notify(self, "CustomizationSelected")


class ShoppingCartMediator(Mediator):
    def __init__(
        self,
        product_item: ProductItem,
        quantity_input: QuantityInput,
        customization: Customization,
    ) -> None:
        self._product_item = product_item
        self._product_item.mediator = self
        self._quantity_input = quantity_input
        self._quantity_input.mediator = self
        self._customization = customization
        self._customization.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "CustomizationSelected":
            print(
                "Mediator reacts to customization selection and triggers the following operations:"
            )
            self._quantity_input.update_quantity()


if __name__ == "__main__":
    # Client code representing an online shopping cart
    product_item = ProductItem()
    quantity_input = QuantityInput()
    customization = Customization()
    shopping_cart_mediator = ShoppingCartMediator(
        product_item, quantity_input, customization
    )

    print("User adds a product to the cart.")
    product_item.display()

    print("\n", end="")

    print("User selects customization option.")
    customization.select_option()
