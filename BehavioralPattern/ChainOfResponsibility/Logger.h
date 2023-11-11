#ifndef LOGGER_H
#define LOGGER_H

#include <string>

class Logger {
public:
    static const int DEBUG;
    static const int INFO;
    static const int ERROR;

    Logger(int level);
    void set_next_logger(Logger* next);
    void log_message(const std::string& message, int message_level);
    virtual void write(const std::string& message);

private:
    int level;
    Logger* next_logger;
};

#endif
