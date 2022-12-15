package y2021.day1;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SonarIncreasesTest {
    @Test
    void shouldLoad2000Inputs() throws IOException {
        List<Integer> inputs = SonarIncreases.loadInputs();
        assertEquals(2000, inputs.size());
    }

    @Test
    void getResult() throws IOException {
//        long resultStream = SonarIncreases.solveStream();
        long resultLoop = SonarIncreases.solveRegularLoop();
//        assertEquals(resultLoop, resultStream);
    }

    @Test
    void getResult2() throws IOException {
        long resultLoop = SonarIncreases.solveWindowRegularLoop();
        System.out.println("Result is " + resultLoop);
    }
}
