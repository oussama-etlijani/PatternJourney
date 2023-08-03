#include <memory>
#include "DatabaseConnector.hpp"

class Application {
protected:
    std::unique_ptr<DatabaseConnector> connector;
public:
    virtual ~Application() {} // Virtual destructor
    std::string connectToDatabase();
};

class MySQLApplication : public Application {
public:
    MySQLApplication();
};

class PostgreSQLApplication : public Application {
public:
    PostgreSQLApplication();
};
