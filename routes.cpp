#include "crow_all.h"

crow::response greet()
{
    return crow::response{""};
}
crow::response addg(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{""};
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    return crow::response{""};
}