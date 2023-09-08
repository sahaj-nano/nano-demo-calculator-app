#include "crow_all.h"

crow::response greet()
{
    crow::response res;
    res.code = 200;
    res.set_header("Content-Type", "text/plain");
    res.body = "Hello world!";
    
    return res;
}
crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    if (!input || !input.has("first") || !input.has("second")) {
        return crow::response(400, "Invalid JSON format");
    }
    int first = input["first"].i();
    int second = input["second"].i();
    

    int result = first + second;

    crow::json::wvalue response;
    response["result"] = result;

    crow::response res;
    res.code = 200;
    res.set_header("Content-Type", "application/json");
    res.body = crow::json::dump_to_string(response);
    return res;
}
crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
     if (!input || !input.has("first") || !input.has("second")) {
        return crow::response(400, "Invalid JSON format");
    }
    int first = input["first"].i();
    int second = input["second"].i();
    

    int result = first - second;

    crow::json::wvalue response;
    response["result"] = result;

    crow::response res;
    res.code = 200;
    res.set_header("Content-Type", "application/json");
    res.body = crow::json::dump_to_string(response);
    return res;
}
