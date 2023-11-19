#ifndef EMAIL_LOGGER_H
#define EMAIL_LOGGER_H

#include "Logger.h"

class EmailLogger : public Logger {
public:
    EmailLogger(int level, const std::string& email);
    void write(const std::string& message) override;

private:
    std::string email;
};

#endif
