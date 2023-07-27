#include <memory>

class ToyAnimalFactory {
public:
    virtual std::unique_ptr<ToyAnimal> create_toy_animal() = 0; // Pure virtual function
};

// Usage of the ToyAnimalFactory requires a ToyAnimal class. Here's a placeholder for it.
class ToyAnimal {
public:
    ToyAnimal() {}
    virtual ~ToyAnimal() {}
};
