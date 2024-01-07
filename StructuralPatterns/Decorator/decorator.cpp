#include <iostream>
#include <string>

// Component Interface
class Coffee {
public:
    virtual double cost() const = 0;
    virtual ~Coffee() = default;
};

// Concrete Component
class SimpleCoffee : public Coffee {
public:
    double cost() const override {
        return 2.0; // Base cost for a simple coffee
    }
};

// Decorator
class CoffeeDecorator : public Coffee {
protected:
    Coffee* coffee;

public:
    CoffeeDecorator(Coffee* c) : coffee(c) {}

    double cost() const override {
        return coffee->cost();
    }

    virtual ~CoffeeDecorator() {
        delete coffee;
    }
};

// Concrete Decorators
class SugarDecorator : public CoffeeDecorator {
public:
    SugarDecorator(Coffee* c) : CoffeeDecorator(c) {}

    double cost() const override {
        return CoffeeDecorator::cost() + 0.5;
    }
};

class MilkDecorator : public CoffeeDecorator {
public:
    MilkDecorator(Coffee* c) : CoffeeDecorator(c) {}

    double cost() const override {
        return CoffeeDecorator::cost() + 1.0;
    }
};

class FlavorDecorator : public CoffeeDecorator {
private:
    std::string flavor;

public:
    FlavorDecorator(Coffee* c, const std::string& f) : CoffeeDecorator(c), flavor(f) {}

    double cost() const override {
        return CoffeeDecorator::cost() + 1.5;
    }

    std::string getDescription() const {
        return flavor + " " + typeid(*coffee).name();
    }

    ~FlavorDecorator() override = default;
};

// Client Code
void clientCode(const Coffee& coffee) {
    std::cout << "Cost of " << typeid(coffee).name() << ": $" << coffee.cost() << std::endl;
}

int main() {
    // Create a simple coffee
    Coffee* simpleCoffee = new SimpleCoffee();
    clientCode(*simpleCoffee);
    std::cout << "\n";

    // Decorate the simple coffee with sugar
    Coffee* sugarCoffee = new SugarDecorator(simpleCoffee);
    clientCode(*sugarCoffee);
    std::cout << "\n";

    // Decorate the sugar coffee with milk
    Coffee* sugarMilkCoffee = new MilkDecorator(sugarCoffee);
    clientCode(*sugarMilkCoffee);
    std::cout << "\n";

    // Decorate the sugar milk coffee with a flavor
    Coffee* flavoredCoffee = new FlavorDecorator(sugarMilkCoffee, "Vanilla");
    clientCode(*flavoredCoffee);

    // Cleanup
    delete simpleCoffee;
    delete sugarCoffee;
    delete sugarMilkCoffee;
    delete flavoredCoffee;

    return 0;
}
