#include "ConsoleLogger.h"
#include <iostream>

ConsoleLogger::ConsoleLogger(int level) : Logger(level) {}

void ConsoleLogger::write(const std::string& message) {
    std::cout << "Console Logger: " << message << std::endl;
}
