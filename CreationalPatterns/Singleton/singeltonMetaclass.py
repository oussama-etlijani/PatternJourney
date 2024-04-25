class SingletonMeta(type):
    """A type for Singleton classes (overrides __call__)."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        # If the instance already exists, return it
        if cls not in cls._instances:
            # Create the instance if it doesn't exist
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Create two instances
instance1 = SingletonClass()
instance2 = SingletonClass()

# Test the Singleton functionality
instance1.set_value("Singleton Data")
print(instance1.get_value())  # Output: Singleton Data
print(instance2.get_value())  # Output: Singleton Data (same instance as instance1)

# Test the identity (should be true as both are the same instance)
print(instance1 is instance2)  # Output: True
