#include "Logger.h"
#include "ConsoleLogger.h"
#include "FileLogger.h"
#include "EmailLogger.h"

int main() {
    ConsoleLogger console_logger(Logger::DEBUG);
    FileLogger file_logger(Logger::INFO, "app.log");
    EmailLogger email_logger(Logger::ERROR, "admin@example.com");

    console_logger.set_next_logger(&file_logger);
    file_logger.set_next_logger(&email_logger);

    console_logger.log_message("This is a debug message.", Logger::DEBUG);
    console_logger.log_message("This is an info message.", Logger::INFO);
    console_logger.log_message("This is an error message.", Logger::ERROR);

    return 0;
}
