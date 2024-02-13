from singleton import Singleton

# Attempt to create instances using the public static method
first_instance = Singleton.getInstance()
second_instance = Singleton.getInstance()

# Validate that the instances are the same
if first_instance is second_instance:
    print("Both instances are identical:", first_instance)
