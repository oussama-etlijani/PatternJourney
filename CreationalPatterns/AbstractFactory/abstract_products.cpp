#include <iostream>

class ToyAnimal {
public:
    virtual ~ToyAnimal() {} // Virtual destructor
    virtual void interact() = 0; // Pure virtual function
};

class AquaticAnimal : public ToyAnimal {
public:
    void interact() override {
        std::cout << "Aquatic animal interaction" << std::endl;
    }
};

class TerrestrialAnimal : public ToyAnimal {
public:
    void interact() override {
        std::cout << "Terrestrial animal interaction" << std::endl;
    }
};

class AvianAnimal : public ToyAnimal {
public:
    void interact() override {
        std::cout << "Avian animal interaction" << std::endl;
    }
};
