#include "FileLogger.h"
#include <fstream>

FileLogger::FileLogger(int level, const std::string& filename) : Logger(level), filename(filename) {}

void FileLogger::write(const std::string& message) {
    std::ofstream file(filename, std::ios::app);
    if (file.is_open()) {
        file << "File Logger: " << message << "\n";
        file.close();
    }
}
