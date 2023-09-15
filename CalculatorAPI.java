import com.google.gson.Gson;
import com.google.gson.JsonObject;
import spark.Request;
import spark.Response;
import spark.Route;

public class CalculatorAPI {

    private static final Gson gson = new Gson();

    public static void main(String[] args) {
        Spark.get("/calculator/greeting", (req, res) -> "Hello world!");
        Spark.post("/calculator/add", (req, res) -> {
            JsonObject data = gson.fromJson(req.body(), JsonObject.class);
            int first = data.get("first").getAsInt();
            int second = data.get("second").getAsInt();
            int result = first + second;
            return gson.toJson(new JsonObject().put("result", result));
        });
        Spark.post("/calculator/subtract", (req, res) -> {
            JsonObject data = gson.fromJson(req.body(), JsonObject.class);
            int first = data.get("first").getAsInt();
            int second = data.get("second").getAsInt();
            int result = first - second;
            return gson.toJson(new JsonObject().put("result", result));
        });
        Spark.run(port = 8080);
    }
}
