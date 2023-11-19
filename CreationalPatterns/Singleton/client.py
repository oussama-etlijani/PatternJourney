from singleton import Singleton  # Import the Singleton class

# Attempt to create instances using the public static method
first_instance = Singleton.getInstance()
second_instance = Singleton.getInstance()

# Validate that the instances are the same
if first_instance is second_instance:
    print("Both instances are identical:", first_instance)

# This line would raise an exception
# another_instance = Singleton()
import os

directory_path = '/Users/Ouss/PycharmProjects/PatternJourney/BehavioralPattern/ChainOfResponsibility'

if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' does exist.")
else:
    print(f"The directory '{directory_path}' does not exist.")
