import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
@RequestMapping("/calculator")
public class CalculatorApplication {

    public static void main(String[] args) {
        SpringApplication.run(CalculatorApplication.class, args);
    }

    @GetMapping("/greeting")
    public String greeting() {
        return "Hello world!";
    }

    @PostMapping("/add")
    public Result add(@RequestBody Numbers numbers) {
        int result = numbers.getFirst() + numbers.getSecond();
        return new Result(result);
    }

    @PostMapping("/subtract")
    public Result subtract(@RequestBody Numbers numbers) {
        int result = numbers.getFirst() - numbers.getSecond();
        return new Result(result);
    }

    private static class Numbers {
        private int first;
        private int second;

        public int getFirst() {
            return first;
        }

        public void setFirst(int first) {
            this.first = first;
        }

        public int getSecond() {
            return second;
        }

        public void setSecond(int second) {
            this.second = second;
        }
    }

    private static class Result {
        private int result;

        public Result(int result) {
            this.result = result;
        }

        public int getResult() {
            return result;
        }

        public void setResult(int result) {
            this.result = result;
        }
    }
}
