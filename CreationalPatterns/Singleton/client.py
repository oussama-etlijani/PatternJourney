from singeltonMetaclass import SingletonClass
from singleton import Singleton


def main():
    # Test the Singleton class
    # Attempt to create instances using the public static method
    first_instance = Singleton.getInstance()
    second_instance = Singleton.getInstance()

    # Validate that the instances are the same
    if first_instance is second_instance:
        print("Both instances are identical:", first_instance)
    # Test the SingletonClass
    # Create two instances in different variables
    instance1 = SingletonClass()
    instance2 = SingletonClass()

    # Test to see if both instances are actually the same instance
    print("Checking if both instances are the same instance:")
    print("Instance 1 ID:", id(instance1))
    print("Instance 2 ID:", id(instance2))

    # Set a value in instance1 and check if it reflects in instance2
    instance1.set_value("Singleton Data")
    print("\nValue set in instance1: 'Singleton Data'")
    print("Value retrieved from instance2:", instance2.get_value())

    # Assert that both instances are the same
    assert (
            instance1 is instance2
    ), "Error: instance1 and instance2 are not the same instance"
    print("\nAssertion Passed: Both instances are the same.")


if __name__ == "__main__":
    main()
