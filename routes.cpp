#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello World"};
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{second+first};
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{second-first};
}