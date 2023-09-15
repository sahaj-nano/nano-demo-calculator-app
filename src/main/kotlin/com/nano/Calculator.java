import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.StandardCharsets;

import com.google.gson.Gson;

public class JsonToJava {

    public static void main(String[] args) throws IOException {
        // Get the path to the JSON file.
        String pathToJsonFile = "collections/calculator-tests.postman_collection.json";

        // Create a File object for the JSON file.
        File jsonFile = new File();

        // Create a Reader object for the JSON file.
        Reader reader = new InputStreamReader(jsonFile, StandardCharsets.UTF_8);

        // Create a Gson object.
        Gson gson = new Gson();

        // Convert the JSON file to a Java object.
        Object jsonObject = gson.fromJson(reader, Object.class);

        // Get the first number from the JSON object.
        int firstNumber = Integer.parseInt((String) jsonObject.get("firstNumber"));

        // Get the second number from the JSON object.
        int secondNumber = Integer.parseInt((String) jsonObject.get("secondNumber"));

        // Perform addition.
        int sum = firstNumber + secondNumber;

        // Perform subtraction.
        int difference = firstNumber - secondNumber;

        // Print the results.
        System.out.println("The sum is " + sum);
        System.out.println("The difference is " + difference);
    }
}
