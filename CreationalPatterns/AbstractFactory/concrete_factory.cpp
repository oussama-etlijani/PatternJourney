#include <memory>

// Assuming ToyAnimalFactory and ToyAnimal from previous translations
class ToyAnimalFactory {
public:
    virtual std::unique_ptr<ToyAnimal> create_toy_animal() = 0;
};

class ToyAnimal {
public:
    virtual ~ToyAnimal() {}
};

// Definitions for the Shark, Lion, and Eagle classes
class Shark : public ToyAnimal {
    // Shark-specific methods and members here
};

class Lion : public ToyAnimal {
    // Lion-specific methods and members here
};

class Eagle : public ToyAnimal {
    // Eagle-specific methods and members here
};

// Definitions for the concrete factory classes
class AquaticAnimalFactory : public ToyAnimalFactory {
public:
    std::unique_ptr<ToyAnimal> create_toy_animal() override {
        return std::make_unique<Shark>();
    }
};

class TerrestrialAnimalFactory : public ToyAnimalFactory {
public:
    std::unique_ptr<ToyAnimal> create_toy_animal() override {
        return std::make_unique<Lion>();
    }
};

class AvianAnimalFactory : public ToyAnimalFactory {
public:
    std::unique_ptr<ToyAnimal> create_toy_animal() override {
        return std::make_unique<Eagle>();
    }
};
