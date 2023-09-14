#include "crow_all.h"

crow::response greet()
{
    res.status(200)
    return crow::response{"Hello world!"};
}
crow::response add(const crow::request &req)
{
    res.status(200)
    auto input = crow::json::load(req.body);
    return crow::response{"result ":req.body.first+req.body.second};
}
crow::response subtract(const crow::request &req)
{
    res.status(200)
    auto input = crow::json::load(req.body);
    return crow::response{"result ":req.body.first+req.body.second};
}