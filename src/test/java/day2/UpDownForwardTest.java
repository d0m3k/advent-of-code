package day2;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class UpDownForwardTest {
    @Test
    void shouldLoad1000Inputs() throws IOException {
        List<UpDownForward.JourneyData> inputs = UpDownForward.loadInputs();
        assertEquals(1000, inputs.size());
    }

    @Test
    void solve() throws IOException {
        UpDownForward.Solution solution = UpDownForward.solve();
        System.out.println("depth:" + solution.depth+", x= " + solution.x+", mul="+solution.depth*solution.x);
        assertEquals(1893605, solution.depth*solution.x);
    }

    @Test
    void solve2() throws IOException {
        UpDownForward.SolutionWithAim solution = UpDownForward.solveWithAimLoop();
        System.out.println("depth:" + solution.depth+", x= " + solution.x+", mul="+solution.depth*solution.x);
    }
}