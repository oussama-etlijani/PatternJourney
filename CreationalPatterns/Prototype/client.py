from concrete_prototype import ConcretePrototype
from prototype_registry import PrototypeRegistry

if __name__ == "__main__":
    """
    Client code to demonstrate the Prototype design pattern.
    Registers a prototype, clones it through the registry, and confirms the cloned object.
    """
    # Create and register a prototype
    prototype_a = ConcretePrototype("value1", "value2")
    PrototypeRegistry.register_prototype("prototypeA", prototype_a)

    # Clone a prototype from registry
    cloned_prototype = PrototypeRegistry.get_clone("prototypeA")
    print(cloned_prototype)

    # Confirm they are two different objects with the same data
    assert id(prototype_a) != id(cloned_prototype)
    assert str(prototype_a) == str(cloned_prototype)
