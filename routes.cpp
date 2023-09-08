#include "crow_all.h"

crow::response greet()
{
    return crow::response{"Hello world!"};
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    if(!input){
        return crow::response(200,"INVALID JSON");
    }
    int num1=input["num1"].i();
    int num2=input["num2"].i();
    int res=num1+num2;
    return crow::response{crow::json::dump_to_string(res)};
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
     if(!input){
        return crow::response(200,"INVALID JSON");
    }
    int num1=input["num1"].i();
    int num2=input["num2"].i();
    int res=num1-num2;
    return crow::response{crow::json::dump_to_string(res)};
}
