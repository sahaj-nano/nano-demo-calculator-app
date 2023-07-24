#include "crow_all.h"


crow::response greet()
{
    return crow::response{"Hello World!"};
}

crow::response add(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    if (!input)
    {
        // Return an error response when JSON parsing fails
        return crow::response(400, "Bad Request");
    }

    crow::json::wvalue result;
    result["result"] = input["first"].i() + input["second"].i();
    return crow::response{result};
}

crow::response subtract(const crow::request &req)
{
    auto input = crow::json::load(req.body);
    if (!input)
    {
        // Return an error response when JSON parsing fails
        return crow::response(400, "Bad Request");
    }

    crow::json::wvalue result;
    result["result"] = input["first"].i() - input["second"].i();
    return crow::response{result};
}
// With these corrections, the code should now work as intended and handle the "/greet," "/add," and "/subtract" endpoints with proper JSON responses, as well as include basic error handling for JSON parsing issues.






