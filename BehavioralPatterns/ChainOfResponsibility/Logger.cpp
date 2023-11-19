#include "Logger.h"

const int Logger::DEBUG = 1;
const int Logger::INFO = 2;
const int Logger::ERROR = 3;

Logger::Logger(int level) : level(level), next_logger(nullptr) {}

void Logger::set_next_logger(Logger* next) {
    next_logger = next;
}

void Logger::log_message(const std::string& message, int message_level) {
    if (level <= message_level) {
        write(message);
    }
    if (next_logger != nullptr) {
        next_logger->log_message(message, message_level);
    }
}

void Logger::write(const std::string& message) {
    // Base class implementation does nothing
}
