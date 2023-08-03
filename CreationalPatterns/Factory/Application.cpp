#include "Application.hpp"

std::string Application::connectToDatabase() {
    return connector->connect();
}

MySQLApplication::MySQLApplication() {
    connector = std::make_unique<MySQLConnector>();
}

PostgreSQLApplication::PostgreSQLApplication() {
    connector = std::make_unique<PostgreSQLConnector>();
}
