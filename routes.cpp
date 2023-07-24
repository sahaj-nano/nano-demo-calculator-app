#include "crow_all.h"

crow::response greet()
{
    std::string msg="test";
    std::string msg="test2";
    return crow::response{msg};
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{""};
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{""};
}