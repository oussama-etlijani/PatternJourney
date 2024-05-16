from flyweight_factory import FlyweightFactory
from vehicle import Vehicle


def main():
    """
    Main function to demonstrate the use of the Flyweight pattern in client code.
    """
    # Example vehicle data
    vehicle_data = [
        {"model_type": "car", "position": (0, 0), "destination": (10, 10)},
        {"model_type": "bicycle", "position": (1, 1), "destination": (5, 5)},
        {"model_type": "car", "position": (2, 2), "destination": (15, 15)},
        {"model_type": "bicycle", "position": (2, 2), "destination": (15, 15)},
        # Add more vehicle data as needed
    ]

    # Initialize the FlyweightFactory instance to manage flyweight objects.
    factory = FlyweightFactory()

    # List to store the vehicle objects.
    vehicles = []

    # Iterate through the vehicle data to create vehicle objects.
    for data in vehicle_data:
        """
        This loop demonstrates the use of the Flyweight pattern in client code.

        vehicle_data: A list of dictionaries, where each dictionary contains individual vehicle information,
                      including 'model_type', 'position', and 'destination'.

        The Flyweight pattern is used to minimize memory usage by sharing common data (intrinsic state)
        across multiple vehicle objects.
        """

        # Retrieve the flyweight object for the vehicle's model type from the factory.
        flyweight = factory.get_flyweight(data["model_type"])

        # Create a new Vehicle object using the flyweight and the unique extrinsic state (position and destination).
        vehicle = Vehicle(flyweight, data["position"], data["destination"])

        # Add the newly created vehicle to the list of vehicles.
        vehicles.append(vehicle)

    # Simulate rendering and moving the vehicles
    for vehicle in vehicles:
        vehicle.render()
        vehicle.move()


if __name__ == "__main__":
    main()
