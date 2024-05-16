class VehicleFlyweight:
    """
    A class to represent the intrinsic state of a vehicle in a traffic simulation.
    This class implements the Flyweight design pattern by encapsulating properties
    that are shared among multiple vehicle objects.

    Attributes:
        model_type (str): The type of the vehicle (e.g., car, bicycle).
        appearance (str): The visual appearance of the vehicle.
        behavior_rules (str): The behavior rules that the vehicle follows (e.g., speed limits, traffic rules).
    """

    def __init__(self, model_type, appearance, behavior_rules):
        """
        Initializes a new VehicleFlyweight object with the specified model type, appearance, and behavior rules.

        Parameters:
            model_type (str): The type of the vehicle.
            appearance (str): The visual appearance of the vehicle.
            behavior_rules (str): The behavior rules that the vehicle follows.
        """
        self.model_type = model_type
        self.appearance = appearance
        self.behavior_rules = behavior_rules
        print(f"VehicleFlyweight created: {self.model_type}")
