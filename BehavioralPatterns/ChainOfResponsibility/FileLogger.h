#ifndef FILE_LOGGER_H
#define FILE_LOGGER_H

#include "Logger.h"

class FileLogger : public Logger {
public:
    FileLogger(int level, const std::string& filename);
    void write(const std::string& message) override;

private:
    std::string filename;
};

#endif
