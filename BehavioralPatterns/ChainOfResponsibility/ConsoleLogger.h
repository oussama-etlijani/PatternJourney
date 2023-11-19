#ifndef CONSOLE_LOGGER_H
#define CONSOLE_LOGGER_H

#include "Logger.h"

class ConsoleLogger : public Logger {
public:
    ConsoleLogger(int level);
    void write(const std::string& message) override;
};

#endif
