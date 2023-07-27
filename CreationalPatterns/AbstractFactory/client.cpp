#include <iostream>
#include <memory>


class ToyShop {
private:
    std::unique_ptr<ToyAnimalFactory> factory;

public:
    ToyShop(std::unique_ptr<ToyAnimalFactory> factory) : factory(std::move(factory)) {}

    std::string order_toy_animal() {
        std::unique_ptr<ToyAnimal> toy = factory->create_toy_animal();
        return toy->interact();
    }
};

// Client code starts execution here
int main() {
    // An instance of the TerrestrialAnimalFactory is created
    std::unique_ptr<ToyAnimalFactory> factory = std::make_unique<TerrestrialAnimalFactory>();

    // A ToyShop object is created with the factory object as an argument
    ToyShop shop(std::move(factory));

    // The order_toy_animal method of the ToyShop object is called and the returned result is printed to the console
    std::cout << shop.order_toy_animal() << std::endl;  // Outputs: "The lion roars."

    return 0;
}
