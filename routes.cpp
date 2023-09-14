#include "crow_all.h"

crow::response greet()
{
    
    return crow::response{"Hello world!"};
    return crow::response{""};
}
crow::response add(const crow::request &req)
{
    
    auto input = crow::json::load(req.body);
     crow::json::wvalue result;
    result["result"] = input["first"].i() + input["second"].i();
    return result;
    return crow::response{""};
}
crow::response subtract(const crow::request &req)
{
    
    auto input = crow::json::load(req.body);
    crow::json::wvalue result;
    result["result"] = input["first"].i() - input["second"].i();
    return result;
    return crow::response{""};
}