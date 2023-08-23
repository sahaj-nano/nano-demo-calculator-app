#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello world!\n"};
}

crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    
    if (!input)
    {
        return crow::response(400, "Invalid JSON format");
    }

    double first_num = input["first"].d();
    double second_num = input["second"].d();
    double result_num = first_num + second_num;

    crow::json::wvalue response_json;
    response_json["result"] = result;

    return crow::response{response_json};
}

crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    
    if (!input)
    {
        return crow::response(400, "Invalid JSON format");
    }

    double first_num = input["first"].d();
    double second_num = input["second"].d();
    double result_num = first_num - second_num;

    crow::json::wvalue response_json;
    response_json["result"] = result ;

    return crow::response{response_json};
}

int main()
{
    crow::SimpleApp app;

    CROW_ROUTE(app, "/calculator/greeting")
    .methods("GET"_method)
    ([] {
        return greet();
    });

    CROW_ROUTE(app, "/calculator/add")
    .methods("POST"_method)
    ([](const crow::request &req) {
        return add(req);
    });

    CROW_ROUTE(app, "/calculator/subtract")
    .methods("POST"_method)
    ([](const crow::request &req) {
        return subtract(req);
    });

    app.port(8080).multithreaded().run();
    return 0;
}
