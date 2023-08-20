#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello World!"};
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    auto first = int(input["first"]);
    auto second = int(input["second"]);
    crow::json::wvalue x;
    x["result"] = first+second;
    return crow::response(x);
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    auto first = int(input["first"]);
    auto second = int(input["second"]);
    crow::json::wvalue x;
    x["result"] = first-second;
    return crow::response(x);
}