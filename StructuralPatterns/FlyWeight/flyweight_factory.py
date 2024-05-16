from vehicle_flyweight import VehicleFlyweight


class FlyweightFactory:
    """
    A factory class to manage the creation and retrieval of VehicleFlyweight objects.
    This class implements the Flyweight design pattern by maintaining a pool of flyweight objects.

    Attributes:
        _flyweights (dict): A dictionary to store the existing flyweight objects, keyed by model type.
    """

    _flyweights = {}

    @staticmethod
    def get_flyweight(model_type):
        """
        Retrieves an existing VehicleFlyweight object for the specified model type,
        or creates a new one if it does not exist.

        Parameters:
            model_type (str): The type of the vehicle for which to retrieve the flyweight.

        Returns:
            VehicleFlyweight: The flyweight object corresponding to the specified model type.
        """
        if model_type not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[model_type] = (
                FlyweightFactory.create_flyweight(model_type)
            )
            print(f"New flyweight created for model type: {model_type}")
        else:
            print(f"Reusing existing flyweight for model type: {model_type}")
        return FlyweightFactory._flyweights[model_type]

    @staticmethod
    def create_flyweight(model_type):
        """
        Creates a new VehicleFlyweight object for the specified model type.
        Placeholder values are used for appearance and behavior rules.

        Parameters:
            model_type (str): The type of the vehicle for which to create the flyweight.

        Returns:
            VehicleFlyweight: A new flyweight object for the specified model type.
        """
        # Create the flyweight object based on model_type
        appearance = "default_appearance"
        behavior_rules = "default_behavior_rules"
        return VehicleFlyweight(model_type, appearance, behavior_rules)
