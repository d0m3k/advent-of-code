package y2021.day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class UpDownForward {
    private enum Direction {
        UP, DOWN, FORWARD;

        static Direction getDirection(String direction) {
            switch (direction) {
                case "up":
                    return UP;
                case "down":
                    return DOWN;
                case "forward":
                    return FORWARD;
                default:
                    throw new RuntimeException("Direction unknown!");
            }
        }
    }

    static class JourneyData {
        final Direction direction;
        final int value;

        public JourneyData(String direction, int value) {
            this.direction = Direction.getDirection(direction);
            this.value = value;
        }
    }

    static class Solution {
        final int x;
        final int depth;

        Solution(int x, int depth) {
            this.x = x;
            this.depth = depth;
        }

        static Solution add(Solution a, Solution b) {
            return new Solution(a.x + b.x, a.depth + b.depth);
        }


        static Solution journeyToSolution(JourneyData journeyData) {
            int x = 0;
            int depth = 0;
            switch (journeyData.direction) {
                case FORWARD:
                    x = journeyData.value;
                    break;
                case UP:
                    depth = -journeyData.value;
                    break;
                case DOWN:
                    depth = journeyData.value;
            }
            return new Solution(x, depth);
        }
    }

    static class SolutionWithAim extends Solution {
        final int aim;

        SolutionWithAim(int x, int depth, int aim) {
            super(x, depth);
            this.aim = aim;
        }

        static SolutionWithAim add(SolutionWithAim a, SolutionWithAim b) {
            return new SolutionWithAim(a.x + b.x, a.depth + b.depth, a.aim + b.aim);
        }

        static SolutionWithAim journeyToSolutionWithAim(JourneyData journeyData, int currentAim) {
            int x = 0;
            int depth = 0;
            int newAim = 0;
            switch (journeyData.direction) {
                case FORWARD:
                    x = journeyData.value;
                    depth = currentAim * journeyData.value;
                    break;
                case UP:
                    newAim = -journeyData.value;
                    break;
                case DOWN:
                    newAim = journeyData.value;
            }
            return new SolutionWithAim(x, depth, newAim);
        }

    }

    public static final String INPUT_PATH = "y2021/day-2-input";

    public static List<JourneyData> loadInputs() throws IOException {
        List<JourneyData> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(UpDownForward.class.getClassLoader().getResourceAsStream(INPUT_PATH)));
        while (bufferedReader.ready()) {
            String currentLine = bufferedReader.readLine();
            String[] s = currentLine.trim().split(" ");
            result.add(new JourneyData(s[0], Integer.parseInt(s[1])));
        }
        return result;
    }

    public static Solution solve() throws IOException {
        List<JourneyData> journeyData = loadInputs();
        return journeyData.stream()
                .map(Solution::journeyToSolution)
                .reduce(Solution::add)
                .get();
    }

    public static SolutionWithAim solveWithAim() throws IOException {
        List<JourneyData> journeyData = loadInputs();
        return journeyData.stream()
                .reduce(new SolutionWithAim(0, 0, 0),
                        (acc, toAdd) -> SolutionWithAim.journeyToSolutionWithAim(toAdd, acc.aim),
                        SolutionWithAim::add);
    }

    public static SolutionWithAim solveWithAimLoop() throws IOException {
        List<JourneyData> journeyData = loadInputs();
        int x = 0;
        int depth = 0;
        int aim = 0;
        for(JourneyData journey : journeyData) {
            switch (journey.direction) {
                case FORWARD:
                    x += journey.value;
                    depth += aim * journey.value;
                    break;
                case UP:
                    aim -= journey.value;
                    break;
                case DOWN:
                    aim += journey.value;
            }
        }
        return new SolutionWithAim(x, depth, aim);
    }
}
