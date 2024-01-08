#include <iostream>
#include <vector>

// Subsystem components
class CPU {
public:
    std::string start() {
        return "CPU started";
    }
};

class Memory {
public:
    std::string load() {
        return "Memory loaded";
    }
};

class HardDrive {
public:
    std::string read() {
        return "Hard Drive read";
    }
};

// Facade
class ComputerFacade {
private:
    CPU cpu;
    Memory memory;
    HardDrive hardDrive;

public:
    std::vector<std::string> start() {
        std::vector<std::string> result;
        result.push_back(cpu.start());
        result.push_back(memory.load());
        result.push_back(hardDrive.read());
        return result;
    }
};

// Client code
int main() {
    // Using the Facade to start the computer
    ComputerFacade computerFacade;

    // Starting the computer
    std::vector<std::string> result = computerFacade.start();

    // Displaying the result
    std::cout << "Computer Starting Sequence:" << std::endl;
    for (const auto& step : result) {
        std::cout << step << std::endl;
    }

    return 0;
}
