#include "crow_all.h"

// Endpoint to check if the service is available
crow::response greet()
{
    return crow::response{"Hello world!\n"};
}

// Endpoint to add two numbers
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    
    if (!input)
    {
        return crow::response(400, "Invalid JSON format in the request body\n");
    }

    if (!input.has("first") || !input.has("second"))
    {
        return crow::response(400, "Missing 'first' or 'second' parameter in the request body\n");
    }

    double first = input["first"].d();
    double second = input["second"].d();
    double result = first + second;

    crow::json::wvalue response;
    response["result"] = result;

    return crow::response{response};
}

// Endpoint to subtract two numbers
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    
    if (!input)
    {
        return crow::response(400, "Invalid JSON format in the request body\n");
    }

    if (!input.has("first") || !input.has("second"))
    {
        return crow::response(400, "Missing 'first' or 'second' parameter in the request body\n");
    }

    double first = input["first"].d();
    double second = input["second"].d();
    double result = first - second;

    crow::json::wvalue response;
    response["result"] = result;

    return crow::response{response};
}

int main()
{
    crow::SimpleApp app;

    // Define the routes
    CROW_ROUTE(app, "/calculator/greeting").get(&greet);
    CROW_ROUTE(app, "/calculator/add").post(&add);
    CROW_ROUTE(app, "/calculator/subtract").post(&subtract);

    // Start the server on port 8080
    app.port(8080).multithreaded().run();
    
    return 0;
}
