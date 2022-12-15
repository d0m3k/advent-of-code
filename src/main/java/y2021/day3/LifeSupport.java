package y2021.day3;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static y2021.day3.PowerConsumption.loadInputs;


public class LifeSupport {
    static class Solution {
        final String oxygenGeneratorRatingBinary;
        final String co2ScrubberRatingBinary;


        public Solution(Map<Integer, Integer> countOfZerosOxygen, Map<Integer, Integer> countOfOnesOxygen, Map<Integer, Integer> countOfZerosScrubber, Map<Integer, Integer> countOfOnesScrubber) {
            StringBuffer oxygenGenerator = new StringBuffer();
            StringBuffer co2Scrubber = new StringBuffer();
            // oxygen generator
            for (int i = 0; i < countOfOnesOxygen.size(); i++) {
                if (countOfOnesOxygen.get(i) >= countOfZerosOxygen.get(i)) {
                    oxygenGenerator.append("1");
                } else {
                    oxygenGenerator.append("0");
                }
            }
            // co2 scubba
            for (int i = 0; i < countOfOnesScrubber.size(); i++) {
                if (countOfOnesScrubber.get(i) < countOfZerosScrubber.get(i)) {
                    co2Scrubber.append("1");
                } else {
                    co2Scrubber.append("0");
                }
            }


            this.oxygenGeneratorRatingBinary = oxygenGenerator.toString();
            this.co2ScrubberRatingBinary = co2Scrubber.toString();
        }

        @Override
        public String toString() {
            int oxygenGenRating = Integer.parseInt(oxygenGeneratorRatingBinary, 2);
            int co2Scrubber = Integer.parseInt(co2ScrubberRatingBinary, 2);
            return "Solution{" +
                    "oxygenGeneratorRatingBinary='" + oxygenGeneratorRatingBinary + '\'' +
                    ", co2ScrubberRatingBinary='" + co2ScrubberRatingBinary + '\'' +
                    ", oxygenGenRating='" + oxygenGenRating + '\'' +
                    ", co2Scrubber='" + co2Scrubber + '\'' +
                    ", solution='" + oxygenGenRating * co2Scrubber + '\'' +
                    '}';
        }
    }

    public static Solution solve() {
        List<String> lines = loadInputs();
        int outputWidth = lines.get(0).length();
        //oxygen
        Map<Integer, Integer> countOfOnesOxygen = new HashMap<>();
        Map<Integer, Integer> countOfZerosOxygen = new HashMap<>();
        for (int i = 0; i < outputWidth; i++) {
            countOfOnesOxygen.put(i, 0);
            countOfZerosOxygen.put(i, 0);
        }

        for (int i = 0; i < outputWidth && !lines.isEmpty(); i++) {
            if (lines.size() <= 1) {
                for (int j=i; j<outputWidth; j++) {
                    countOfOnesOxygen.remove(j);
                    countOfZerosOxygen.remove(j);
                }
                break;
            }
            for (String line : lines) {
                char j = line.charAt(i);
                if (j == '0') {
                    countOfZerosOxygen.put(i, countOfZerosOxygen.get(i) + 1);
                } else {
                    countOfOnesOxygen.put(i, countOfOnesOxygen.get(i) + 1);
                }
            }
            if (countOfOnesOxygen.get(i) >= countOfZerosOxygen.get(i)) {
                lines = keep(lines, i, 1);
            } else {
                lines = keep(lines, i, 0);
            }
        }

        // scubber
        lines = loadInputs();
        Map<Integer, Integer> countOfOnesScrubber = new HashMap<>();
        Map<Integer, Integer> countOfZerosScrubber = new HashMap<>();
        for (int i = 0; i < outputWidth; i++) {
            countOfOnesScrubber.put(i, 0);
            countOfZerosScrubber.put(i, 0);
        }

        for (int i = 0; i < outputWidth && !lines.isEmpty(); i++) {
            if(lines.size() <= 1) {
                for (int j=i; j<outputWidth; j++) {
                    countOfOnesScrubber.remove(j);
                    countOfZerosScrubber.remove(j);
                }
                break;
            }
            for (String line : lines) {
                char j = line.charAt(i);
                if (j == '0') {
                    countOfZerosScrubber.put(i, countOfZerosScrubber.get(i) + 1);
                } else {
                    countOfOnesScrubber.put(i, countOfOnesScrubber.get(i) + 1);
                }
            }
            if (countOfOnesScrubber.get(i) < countOfZerosScrubber.get(i)) {
                lines = keep(lines, i, 1);
            } else {
                lines = keep(lines, i, 0);
            }
        }
        return new Solution(countOfZerosOxygen, countOfOnesOxygen, countOfZerosScrubber, countOfOnesScrubber);
    }

    private static List<String> keep(List<String> lines, int index, int valueToKeep) {
        Stream<String> stringStream = lines.stream()
                .filter(line -> line.charAt(index) == valueToKeep+48); // remember that valueToKeep is int, but char is char – and ASCII '0' is 48 x))
        List<String> result = stringStream.collect(Collectors.toList());
        System.out.println("Ending with lines count: " + result.size() + " at index " +index);
        return result;
    }


}
