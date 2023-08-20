#pragma once
#include "Prototype.h"
#include <string>

class ConcretePrototype : public Prototype {
private:
    std::string attribute1;
    std::string attribute2;

public:
    ConcretePrototype(const std::string& attr1, const std::string& attr2)
        : attribute1(attr1), attribute2(attr2) {}

    ConcretePrototype* clone() const override {
        return new ConcretePrototype(attribute1, attribute2);
    }

    std::string toString() const {
        return "ConcretePrototype(attribute1=" + attribute1 + ", attribute2=" + attribute2 + ")";
    }
};
