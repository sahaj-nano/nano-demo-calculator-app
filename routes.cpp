#include "crow_all.h"

crow::response greet()
{
    return crow::response{"hello world!"};
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
    response_json["result"] = result_num;

    return crow::response{response_json};
}

crow::response subtract(const crow::request &req){

    auto input = crow::json::load(req.body);

    if(!input){
        return crow::response(400, "Invalid JSON format");
    }

    double first_num = input["first"].d();
    double second_num = input["second"].d();
    double result_num = first_num + second_num;

    crow::json::wvalue response_json;

    response_json["result"] = result_num;

    return crow::response{response_json};
}

