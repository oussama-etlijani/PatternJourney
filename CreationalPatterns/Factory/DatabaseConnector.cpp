#include "DatabaseConnector.hpp"

std::string MySQLConnector::connect() const {
    return "MySQL Database connection established";
}

std::string PostgreSQLConnector::connect() const {
    return "PostgreSQL Database connection established";
}
