#include "EmailLogger.h"
#include <iostream>

EmailLogger::EmailLogger(int level, const std::string& email) : Logger(level), email(email) {}

void EmailLogger::write(const std::string& message) {
    std::cout << "Email Logger: Sending email to " << email << " with message: " << message << std::endl;
}
