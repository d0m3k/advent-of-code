package day1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class SonarIncreases {
    public static final String INPUT_PATH = "day-1-input";

    private SonarIncreases(){}
    public static List<Integer> loadInputs() throws IOException {
        List<Integer> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(SonarIncreases.class.getClassLoader().getResourceAsStream(INPUT_PATH)));
        while (bufferedReader.ready()) {
            String currentLine = bufferedReader.readLine();
            result.add(Integer.parseInt(currentLine));
        }
        return result;
    }

    public static long solveStream() throws IOException {
        List<Integer> inputs = loadInputs();
        var lambdaContext = new Object() {
            int currentOne = Integer.MAX_VALUE;
            int previousOne = Integer.MAX_VALUE;
        };
        return inputs.stream()
                .peek(x -> {
                    System.out.println("Now going through " + x);
                    lambdaContext.currentOne = x;
                    if (lambdaContext.previousOne<Integer.MAX_VALUE) {
                        lambdaContext.previousOne = lambdaContext.currentOne;
                    }
                })
                .filter(x -> x>lambdaContext.previousOne)
                .count();
    }

    public static long solveRegularLoop() throws IOException {
        List<Integer> inputs = loadInputs();
        long result = 0;
        for(int i=1; i<inputs.size();i++) {
            if(inputs.get(i) > inputs.get(i-1)) {
                result++;
            }
        }
        return result;
    }

    public static long solveWindowRegularLoop() throws IOException {
        List<Integer> inputs = loadInputs();
        long result = 0;
        int currentSum, previousSum;
        for(int i=3; i<inputs.size();i++) {
            previousSum = inputs.get(i-3)+ inputs.get(i-2) + inputs.get(i-1);
            currentSum = inputs.get(i-2) + inputs.get(i-1) + inputs.get(i);
            if(currentSum > previousSum) {
                result++;
            }
        }
        return result;
    }
}
