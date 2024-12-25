include <iostream>

// Forward declarations
class ProductItem;
class QuantityInput;
class Customization;

// Mediator interface
class Mediator {
public:
    virtual void notify(BaseComponent* sender, const std::string& event) = 0;
};

// Base Component class
class BaseComponent {
protected:
    Mediator* mediator;

public:
    BaseComponent(Mediator* mediator = nullptr) : mediator(mediator) {}

    void setMediator(Mediator* mediator) {
        this->mediator = mediator;
    }
};

// Concrete Components
class ProductItem : public BaseComponent {
public:
    void display() {
        std::cout << "Displaying product details." << std::endl;
    }
    // Other product-related functionality
};

class QuantityInput : public BaseComponent {
public:
    void updateQuantity() {
        std::cout << "Updating quantity based on customization." << std::endl;
        // Additional logic related to quantity updates
    }
};

class Customization : public BaseComponent {
public:
    void selectOption() {
        std::cout << "Customization option selected." << std::endl;
        mediator->notify(this, "CustomizationSelected");
    }
};

// Concrete Mediator
class ShoppingCartMediator : public Mediator {
private:
    ProductItem* productItem;
    QuantityInput* quantityInput;
    Customization* customization;

public:
    ShoppingCartMediator(ProductItem* productItem, QuantityInput* quantityInput, Customization* customization)
        : productItem(productItem), quantityInput(quantityInput), customization(customization) {
        productItem->setMediator(this);
        quantityInput->setMediator(this);
        customization->setMediator(this);
    }

    void notify(BaseComponent* sender, const std::string& event) override {
        if (event == "CustomizationSelected") {
            std::cout << "Mediator reacts to customization selection and triggers the following operations:" << std::endl;
            quantityInput->updateQuantity();
        }
    }
};

int main() {
    // Client code representing an online shopping cart
    ProductItem productItem;
    QuantityInput quantityInput;
    Customization customization;
    ShoppingCartMediator shoppingCartMediator(&productItem, &quantityInput, &customization);

    std::cout << "User adds a product to the cart." << std::endl;
    productItem.display();

    std::cout << "\n";

    std::cout << "User selects customization option." << std::endl;
    customization.selectOption();

    return 0;
}
