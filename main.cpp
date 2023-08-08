#include "crow_all.h"
#include "routes.cpp"
#include <string>
#include <iostream>
int main()
{
  crow::SimpleApp app;
  CROW_ROUTE(app, "/calculator/greeting")
      .methods("GET"_method)(&greet);
  CROW_ROUTE(app, "/calculator/add")
      .methods("POST"_method)(&add);
  CROW_ROUTE(app, "/calculator/subtract")
      .methods("POST"_method)(&subtract);
    cout<<"Hello";
  app.port(8080).run();
  return 0;
}