#ifndef SINGLETON_H
#define SINGLETON_H

class Singleton {
private:
    static Singleton* instance;  // Private static field to store the singleton instance
    Singleton() {}  // Private constructor

public:
    // Public static method to get the singleton instance
    static Singleton* getInstance() {
        if (instance == nullptr) {  // Lazy initialization
            instance = new Singleton();  // Call the private constructor
        }
        return instance;
    }
};

// Initialize the static instance pointer as nullptr
Singleton* Singleton::instance = nullptr;

#endif // SINGLETON_H
