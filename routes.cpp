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

    std::ostringstream oss;
    oss << "{\"result\":" << result << "}";

    // Return the response with status code 200 and JSON content
    crow::response res;
    res.code = 200;
    res.set_header("Content-Type", "application/json");
    res.body = oss.str();

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

    std::ostringstream oss;
    oss << "{\"result\":" << result << "}";

    // Return the response with status code 200 and JSON content
    crow::response res;
    res.code = 200;
    res.set_header("Content-Type", "application/json");
    res.body = oss.str();

    return res;
}
