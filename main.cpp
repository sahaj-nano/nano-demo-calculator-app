#include "crow_all.h"
#include "routes.cpp"
#include <string>
#include <iostream>
int main()
{
    string statusCode;

  crow::SimpleApp app;
  statusCode = apiContractObject.GetStatusCode();
  cout << "Code: " << statusCode << endl
  CROW_ROUTE(app, "/calculator/greeting")
      .methods("GET"_method)(&greet);

    cout << "Status code: " << statusCode << endl;
  CROW_ROUTE(app, "/calculator/add")
      .methods("POST"_method)(&add);
      
      cout << "Status code: " << statusCode << endl;
  CROW_ROUTE(app, "/calculator/subtract")
      .methods("POST"_method)(&subtract);

  app.port(8080).run();
  return 0;
}