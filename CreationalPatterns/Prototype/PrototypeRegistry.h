#pragma once
#include "ConcretePrototype.h"
#include <map>

class PrototypeRegistry {
private:
    static std::map<std::string, ConcretePrototype*> prototypes;

public:
    static void registerPrototype(const std::string& tag, ConcretePrototype* prototype) {
        prototypes[tag] = prototype;
    }

    static ConcretePrototype* getClone(const std::string& tag) {
        if (prototypes.find(tag) != prototypes.end()) {
            return prototypes[tag]->clone();
        }
        return nullptr;
    }

    // Clean-up if needed
    static void clearRegistry() {
        for (auto& prototypePair : prototypes) {
            delete prototypePair.second;
        }
        prototypes.clear();
    }
};

// Define static member outside the class
std::map<std::string, ConcretePrototype*> PrototypeRegistry::prototypes;
