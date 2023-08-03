#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello world!"};
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{input.first + input.second};
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{input.first - input.second};
}
