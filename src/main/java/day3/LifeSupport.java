package day3;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static day3.PowerConsumption.loadInputs;

public class LifeSupport {
    static class Solution {
        final String oxygenGeneratorRatingBinary;
        final String co2ScrubberRatingBinary;


        public Solution(Map<Integer, Integer> countOfZerosOxygen, Map<Integer, Integer> countOfOnesOxygen, Map<Integer, Integer> countOfZerosScrubber, Map<Integer, Integer> countOfOnesScrubber, int outputWidth) {
            StringBuffer oxygenGenerator = new StringBuffer();
            StringBuffer co2Scrubber = new StringBuffer();
            // oxygen generator
            for (int i = 0; i < outputWidth; i++) {
                if (countOfOnesOxygen.get(i) >= countOfZerosOxygen.get(i)) {
                    oxygenGenerator.append("1");
                } else {
                    oxygenGenerator.append("0");
                }
            }
            // co2 scubba
            for (int i = 0; i < outputWidth; i++) {
                if (countOfOnesScrubber.get(i) < countOfZerosScrubber.get(i)) {
                    oxygenGenerator.append("1");
                } else {
                    oxygenGenerator.append("0");
                }
            }


            this.oxygenGeneratorRatingBinary = oxygenGenerator.toString();
            this.co2ScrubberRatingBinary = co2Scrubber.toString();
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

    public static PowerConsumption.Solution solve() {
        List<String> lines = loadInputs();
        int outputWidth = lines.get(0).length();
        //oxygen
        Map<Integer, Integer> countOfOnesOxygen = new HashMap<>();
        Map<Integer, Integer> countOfZerosOxygen = new HashMap<>();
        for (int i = 0; i < outputWidth; i++) {
            countOfOnesOxygen.put(i, 0);
            countOfZerosOxygen.put(i, 0);
        }

        for (int i = 0; i < outputWidth && lines.size()>1; i++) {
            for (String line : lines) {
                char j = line.charAt(i);
                if (j == '0') {
                    countOfZerosOxygen.put(i, countOfZerosOxygen.get(i) + 1);
                } else {
                    countOfOnesOxygen.put(i, countOfOnesOxygen.get(i) + 1);
                }
            }
            if (countOfOnesOxygen.get(i) >= countOfZerosOxygen.get(i)) {
                lines = prune(lines, i, 0);
            } else {
                lines = prune(lines, i, 1);
            }
        }
        return new PowerConsumption.Solution(countOfZeros, countOfOnes, outputWidth);
    }
}
