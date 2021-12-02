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
        UpDownForward.Solution solve = UpDownForward.solve();
        System.out.println("depth:" + solve.depth+", x= " + solve.x+", mul="+solve.depth*solve.x);
        assertEquals(1893605, solve.depth*solve.x);
    }
}