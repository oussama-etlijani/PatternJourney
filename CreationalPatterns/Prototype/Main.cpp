#include "ConcretePrototype.h"
#include "PrototypeRegistry.h"
#include <iostream>

int main() {
    // Register a prototype
    ConcretePrototype prototypeA("value1", "value2");
    PrototypeRegistry::registerPrototype("prototypeA", &prototypeA);

    // Clone from registry
    ConcretePrototype* clonedPrototype = PrototypeRegistry::getClone("prototypeA");
    if (clonedPrototype) {
        std::cout << clonedPrototype->toString() << std::endl;
        delete clonedPrototype;
    }

    // Cleanup
    PrototypeRegistry::clearRegistry();

    return 0;
}
