class Singleton:
    _instance = None  # Private static field to store the singleton instance

    @staticmethod
    def getInstance():
        """Public static method to get the singleton instance."""
        if Singleton._instance is None:  # Lazy initialization
            Singleton._instance = Singleton()  # Call the private constructor
        return Singleton._instance

    def __init__(self):
        """Private constructor."""
        if Singleton._instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            Singleton._instance = self
