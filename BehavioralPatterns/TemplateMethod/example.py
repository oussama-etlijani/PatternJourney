from abc import ABC, abstractmethod


# Abstract base class defining the template method and structure of food preparation.
class FoodPreparation(ABC):
    def prepare_food(self):
        """
        Template method defining the steps of food preparation.
        This method ensures that the steps are executed in the correct order.
        """
        self.gather_ingredients()  # Step 1: Gather ingredients
        self.cook()  # Step 2: Cook the food
        self.serve()  # Step 3: Serve the dish

    @abstractmethod
    def gather_ingredients(self):
        """
        Abstract method to be implemented by subclasses to specify how ingredients are gathered.
        """
        pass

    @abstractmethod
    def cook(self):
        """
        Abstract method to be implemented by subclasses to specify the cooking process.
        """
        pass

    def serve(self):
        """
        Optional step with a default implementation for serving the food.
        Subclasses can override this if needed.
        """
        print("Serving the dish on a plate.")


# Concrete class for preparing pasta, implementing the specific steps for pasta preparation.
class PastaPreparation(FoodPreparation):
    def gather_ingredients(self):
        """
        Specifies the ingredients required for making pasta.
        """
        print("Gathering pasta, olive oil, garlic, and parmesan.")

    def cook(self):
        """
        Specifies the cooking process for pasta.
        """
        print("Boiling pasta and sautéing garlic in olive oil.")


# Concrete class for preparing salad, implementing the specific steps for salad preparation.
class SaladPreparation(FoodPreparation):
    def gather_ingredients(self):
        """
        Specifies the ingredients required for making a salad.
        """
        print("Gathering lettuce, tomatoes, cucumbers, and dressing.")

    def cook(self):
        """
        Specifies the 'cooking' process for salad (tossing the ingredients together).
        """
        print("Tossing vegetables with dressing.")

    def serve(self):
        """
        Customizes the serving process for salad.
        """
        print("Serving the salad in a bowl.")


# Example usage of the Template Method Pattern
if __name__ == "__main__":
    print("Preparing pasta:")
    pasta = PastaPreparation()
    pasta.prepare_food()  # Execute the template method for pasta preparation

    print("\nPreparing salad:")
    salad = SaladPreparation()
    salad.prepare_food()  # Execute the template method for salad preparation
