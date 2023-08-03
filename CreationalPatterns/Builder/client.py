from builder import ConcreteBuilder1
from director import Director

# Client's code
def client_code(director):
    director.construct_basic_vehicle()
    vehicle = director.get_vehicle()
    print(f"Vehicle constructed with parts: {vehicle.list_parts()}")


if __name__ == "__main__":
    # This code will only be run if this file is the entry point of your program.

    # Create builder and director instances
    from builder import ConcreteBuilder1
    from director import Director

    builder = ConcreteBuilder1()
    director = Director(builder)

    # Use director to construct vehicles
    client_code(director)