#include <iostream>
#include "Singleton.h"  // Include the Singleton class definition

int main() {
    // Attempt to create instances using the public static method
    Singleton* firstInstance = Singleton::getInstance();
    Singleton* secondInstance = Singleton::getInstance();

    // Validate that the instances are the same
    if (firstInstance == secondInstance) {
        std::cout << "Both instances are identical: " << firstInstance << std::endl;
    }

    return 0;
}
