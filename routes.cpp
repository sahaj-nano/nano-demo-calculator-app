#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello world!"}.code(crow::HTTPStatus::OK); 
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
   int first = input["first"].i();
    int second = input["second"].i();
    int result = first + second;

    crow::json::wvalue response;
    response["result"] = result;

    return crow::response{response};
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    int first = input["first"].i();
    int second = input["second"].i();
    int result = first - second;

    crow::json::wvalue response;
    response["result"] = result;

    return crow::response{response};
}
