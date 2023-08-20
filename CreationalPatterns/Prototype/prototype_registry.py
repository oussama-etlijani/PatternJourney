

class PrototypeRegistry:
    """
    Maintains a registry of prototypes for cloning.
    Allows for registering, fetching, and listing prototypes.
    """
    _prototypes = {}

    @classmethod
    def register_prototype(cls, tag, prototype):
        """
        Register a prototype with a specific tag.

        Parameters:
        - tag: str
        - prototype: ConcretePrototype object
        """
        cls._prototypes[tag] = prototype

    @classmethod
    def get_clone(cls, tag):
        """
        Fetch and clone a prototype based on the given tag.

        Parameters:
        - tag: str

        Returns:
        - ConcretePrototype object (if found)

        Raises:
        - ValueError: If no prototype found for the given tag.
        """
        prototype = cls._prototypes.get(tag)
        if prototype:
            return prototype.clone()
        raise ValueError(f"No prototype found for tag: {tag}")

    @classmethod
    def list_prototypes(cls):
        """
        List all registered prototype tags.

        Returns:
        - List of tags (str)
        """
        return cls._prototypes.keys()
