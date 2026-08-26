package tests;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static utils.GameUtils.sort;

public class GameUtilsTest {

    private int[] numberArray;

    @BeforeEach
    void setUp() {
        numberArray = new int[]{7, 2, 0, 7, 8};
    }

    @AfterEach
    void tearDown() {
        numberArray = null;
    }

    @Test
    void testSort() {
        int[] sortedArray = new int[]{0, 2, 7, 7, 8};
        sort(numberArray);
        assertArrayEquals(sortedArray, numberArray);
    }
}
