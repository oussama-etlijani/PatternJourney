#include <iostream>
#include <vector>
#include <memory>

// Component
class FileSystemComponent {
public:
    virtual ~FileSystemComponent() = default;
    virtual std::string display(std::string indent = "") const = 0;
};

// Leaf
class File : public FileSystemComponent {
public:
    File(std::string name) : name(std::move(name)) {}

    std::string display(std::string indent = "") const override {
        return indent + "File: " + name + "\n";
    }

private:
    std::string name;
};

// Composite
class Directory : public FileSystemComponent {
public:
    Directory(std::string name) : name(std::move(name)) {}

    void add(std::shared_ptr<FileSystemComponent> component) {
        children.push_back(std::move(component));
    }

    void remove(const std::shared_ptr<FileSystemComponent>& component) {
        children.erase(std::remove(children.begin(), children.end(), component), children.end());
    }

    std::string display(std::string indent = "") const override {
        std::string result = indent + "Directory: " + name + "\n";
        for (const auto& child : children) {
            result += child->display(indent + "  ");
        }
        return result;
    }

private:
    std::string name;
    std::vector<std::shared_ptr<FileSystemComponent>> children;
};

int main() {
    // Creating leaf objects (Files)
    auto file1 = std::make_shared<File>("Document1.txt");
    auto file2 = std::make_shared<File>("Image.jpg");
    auto file3 = std::make_shared<File>("Spreadsheet.xlsx");

    // Creating composite object (Directory)
    auto rootDirectory = std::make_shared<Directory>("Root");

    // Adding leaf objects to the composite
    rootDirectory->add(file1);
    rootDirectory->add(file2);

    // Creating a subdirectory
    auto subdirectory = std::make_shared<Directory>("Subfolder");
    subdirectory->add(file3);

    // Adding the subdirectory to the root directory
    rootDirectory->add(subdirectory);

    // Displaying the entire file system structure
    std::cout << "File System Structure:\n" << rootDirectory->display();

    return 0;
}
