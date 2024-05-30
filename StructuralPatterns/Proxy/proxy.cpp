#include <iostream>
#include <string>
#include <memory>

// Abstract base class defining the interface for Image
class Image {
public:
    virtual ~Image() = default;
    virtual void display() = 0;
};

// The real object that we want to proxy. It performs the actual image loading and displaying.
class RealImage : public Image {
public:
    RealImage(const std::string& filename) : filename(filename) {
        loadImageFromDisk();  // Load the image from disk upon initialization
    }

    void display() override {
        std::cout << "Displaying " << filename << std::endl;  // Simulate displaying the image
    }

private:
    std::string filename;

    void loadImageFromDisk() {
        std::cout << "Loading image from " << filename << std::endl;  // Simulate loading image from disk
    }
};

// The proxy class, which controls access to the RealImage object
class ProxyImage : public Image {
public:
    ProxyImage(const std::string& filename) : filename(filename), realImage(nullptr) {}

    void display() override {
        if (realImage == nullptr) {
            realImage = std::make_unique<RealImage>(filename);  // Lazy initialization of RealImage
        }
        realImage->display();  // Delegate the display method to the RealImage
    }

private:
    std::string filename;
    std::unique_ptr<RealImage> realImage;
};

int main() {
    ProxyImage image1("photo1.jpg");
    ProxyImage image2("photo2.jpg");

    // Images will be loaded only when display is called for the first time
    image1.display();  // Loads and displays photo1.jpg
    image2.display();  // Loads and displays photo2.jpg
    image1.display();  // Only displays photo1.jpg, without loading again

    return 0;
}
