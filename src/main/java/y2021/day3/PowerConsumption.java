package y2021.day3;

import day1.SonarIncreases;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PowerConsumption {
    public static final String INPUT_PATH = "y2021/day-3-input";

    static class Solution {
        final String epsilonInBinary;
        final String gammaInBinary;

        public Solution(String epsilonInBinary, String gammaInBinary) {
            this.epsilonInBinary = epsilonInBinary;
            this.gammaInBinary = gammaInBinary;
        }

        public Solution(Map<Integer, Integer> countOfZeros, Map<Integer, Integer> countOfOnes, int outputWidth) {
            StringBuffer gamma = new StringBuffer();
            StringBuffer epsilon = new StringBuffer();

            for (int i = 0; i < outputWidth; i++) {
                if (countOfOnes.get(i) > countOfZeros.get(i)) {
                    gamma.append("1");
                    epsilon.append("0");
                } else {
                    gamma.append("0");
                    epsilon.append("1");
                }
            }

            this.epsilonInBinary = epsilon.toString();
            this.gammaInBinary = gamma.toString();
        }

        @Override
        public String toString() {
            int epsilon = Integer.parseInt(epsilonInBinary, 2);
            int gamma = Integer.parseInt(gammaInBinary, 2);
            return "Solution{" +
                    "epsilonInBinary='" + epsilonInBinary + '\'' +
                    ", gammaInBinary='" + gammaInBinary + '\'' +
                    ", epsilon='" + epsilon + '\'' +
                    ", gamma='" + gamma + '\'' +
                    ", solution='" + epsilon * gamma + '\'' +
                    '}';
        }
    }

    public static List<String> loadInputs() {
        List<String> result = new ArrayList<>();
        try (BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(Objects.requireNonNull(SonarIncreases.class.getClassLoader().getResourceAsStream(INPUT_PATH))))) {
            while (bufferedReader.ready()) {
                String currentLine = bufferedReader.readLine();
                result.add(currentLine);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return result;
    }

    public static Solution solve() {
        List<String> lines = loadInputs();
        int outputWidth = lines.get(0).length();
        Map<Integer, Integer> countOfOnes = new HashMap<>();
        Map<Integer, Integer> countOfZeros = new HashMap<>();
        for (int i = 0; i < outputWidth; i++) {
            countOfOnes.put(i, 0);
            countOfZeros.put(i, 0);
        }
        for (String line : lines) {
            for (int i = 0; i < outputWidth; i++) {
                char j = line.charAt(i);
                if (j == '0') {
                    countOfZeros.put(i, countOfZeros.get(i) + 1);
                } else {
                    countOfOnes.put(i, countOfOnes.get(i) + 1);
                }
            }
        }
        return new Solution(countOfZeros, countOfOnes, outputWidth);
    }
}
