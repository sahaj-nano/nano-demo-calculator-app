#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello World!"};
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    crow::json::wvalue result;
    result["result"] = input["first"].i() + input["second"].i();
    return result;
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    crow::json::wvalue result;
    result["result"] = input["first"].i() - input["second"].i();
    return result;
}