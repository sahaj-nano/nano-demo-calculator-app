#include <httplib.h>

using namespace httplib;

const int PORT = 8080;
const std::string baseUrl = "/calculator";

int main() {
    Server server;

    server.Get((baseUrl + "/greeting").c_str(), [](const Request& req, Response& res) {
        res.status = 200;
        res.set_content("Hello World!", "text/plain");
    });

    server.Post((baseUrl + "/add").c_str(), [](const Request& req, Response& res) {
        res.status = 200;
        int first = std::stoi(req.get_param_value("first"));
        int second = std::stoi(req.get_param_value("second"));
        int result = first + second;
        res.set_content(std::to_string(result), "application/json");
    });

    server.Post((baseUrl + "/subtract").c_str(), [](const Request& req, Response& res) {
        res.status = 200;
        int first = std::stoi(req.get_param_value("first"));
        int second = std::stoi(req.get_param_value("second"));
        int result = first - second;
        res.set_content(std::to_string(result), "application/json");
    });

    server.listen("0.0.0.0", PORT);

    std::cout << "Server running at PORT " << PORT << std::endl;

    return 0;
}
