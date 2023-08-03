#include <string>

class DatabaseConnector {
public:
    virtual std::string connect() const = 0; // Pure virtual function makes this class abstract
};

class MySQLConnector : public DatabaseConnector {
public:
    std::string connect() const override;
};

class PostgreSQLConnector : public DatabaseConnector {
public:
    std::string connect() const override;
};
