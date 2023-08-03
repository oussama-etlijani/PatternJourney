#include <iostream>
#include "Application.hpp"

void client_code(Application& app) {
    std::cout << app.connectToDatabase() << std::endl;
}

int main() {
    MySQLApplication mysqlApp;
    client_code(mysqlApp);

    PostgreSQLApplication postgresApp;
    client_code(postgresApp);

    return 0;
}
