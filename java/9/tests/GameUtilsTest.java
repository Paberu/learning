package tests;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static utils.GameUtils.generate;
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

    @Test
    void testHugeArray() {
        int[] hugeArray = generate(1000, 100);
        int[] copyOfHugeArray = Arrays.copyOf(hugeArray, hugeArray.length);
        sort(hugeArray);
        Arrays.sort(copyOfHugeArray);
        assertArrayEquals(copyOfHugeArray, hugeArray);
    }

    @Test
    void testEmpty() {
        int[] noArray = new int[]{};
        sort(noArray);
        assertArrayEquals(new int[]{}, noArray);
    }


}
