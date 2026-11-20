package PowerSet;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

public class PowerSet_3 {

    PowerSet set1;
    PowerSet set2;
    PowerSet set3;
    PowerSet set4;
    Bag bag;

    @BeforeEach
    void setUp() {
        set1 = new PowerSet();
        set2 = new PowerSet();
        set3 = new PowerSet();
        set4 = new PowerSet();
        bag = new Bag();

        set2.put("One and only");

        for (int i = 0; i < 10; i++) {
            set3.put("Little" + i);
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                set4.put("Big" + i + j);
            }
        }

        for (int i = 0; i < 10; i++) {
            bag.put("Bag0" + i);
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                bag.put("Bag" + i + j);
            }
        }
    }

    @Test
    void testPutNew() {
        set1.put("First");
        set1.put("Second");
        assertTrue(set1.get("First"));
        assertTrue(set1.get("Second"));
        assertFalse(set1.get("Third"));
        assertEquals(2, set1.size());
    }

    @Test
    void testPutDuplicate() {
        set2.put("One and only");
        assertTrue(set2.get("One and only"));
        assertEquals(1, set2.size());
    }

    @Test
    void testRemoveFromEmpty() {
        assertFalse(set1.remove("First"));
    }

    @Test
    void testRemoveTheLastOne() {
        assertTrue(set2.remove("One and only"));
        assertEquals(0, set2.size());
    }

    @Test
    void testSimpleRemove() {
        assertTrue(set3.remove("Little5"));
        assertEquals(9, set3.size());
    }

    @Test
    void testManyRemoves() {
        for(int i = 0; i < 10; i++) {
            assertTrue(set4.remove("Big0" + i));
        }
        assertEquals(90, set4.size());
    }

    @Test
    void testIntersection() {
        PowerSet set = new PowerSet();
        for (int i = 4; i < 8; i++) {
            set.put("Little" + i);
        }
        PowerSet resultSet = set.intersection(set3);
        assertEquals(4, resultSet.size());
        for (int i = 0; i < 4; i++) {
            assertFalse(resultSet.get("Little" + i));
        }
        for (int i = 4; i < 8; i++) {
            assertTrue(resultSet.get("Little" + i));
        }
    }

    @Test
    void testIntersectionWithEmpty() {
        PowerSet resultSet = set1.intersection(set2);
        assertEquals(0, resultSet.size());
        assertFalse(resultSet.get("One and only"));
    }

    @Test
    void testIntersection2() {
        PowerSet resultSet = set3.intersection(set4);
        assertEquals(0, resultSet.size());
        assertFalse(resultSet.get("Little9"));
    }

    @Test
    void testUnionWithEmpty() {
        PowerSet resultSet = set1.union(set2);
        assertEquals(1, resultSet.size());
        assertTrue(resultSet.get("One and only"));
    }

    @Test
    void testUnion() {
        PowerSet resultSet = set3.union(set4);
        assertEquals(110, resultSet.size());
        assertTrue(resultSet.get("Little9"));
        assertTrue(resultSet.get("Big23"));
        assertFalse(resultSet.get("Little11"));
    }

    @Test
    void testDifferenceWithEmpty() {
        PowerSet resultSet = set2.difference(set1);
        assertEquals(1, resultSet.size());
        assertTrue(resultSet.get("One and only"));
    }

    @Test
    void testDifference() {
        PowerSet set = new PowerSet();
        for (int i = 0; i < 5; i++) {
            set.put("Little" + i);
        }
        PowerSet resultSet = set3.difference(set);
        assertEquals(5, resultSet.size());
        for (int i = 0; i < 5; i++) {
            assertFalse(resultSet.get("Little" + i));
        }
        for (int i = 5; i < 10; i++) {
            assertTrue(resultSet.get("Little" + i));
        }
    }

    @Test
    void testIsSubsetEmpty() {
        assertTrue(set2.isSubset(set1));
    }

    @Test
    void testIsSubset() {
        assertFalse(set4.isSubset(set3));
    }

    @Test
    void testIsSubsetWithSemisub() {
        PowerSet set = new PowerSet();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                set.put("Big" + i + j);
            }
        }
        set.put("Big!");
        assertFalse(set4.isSubset(set));
    }

    @Test
    void testEqualsSetYes() {
        PowerSet set = new PowerSet();
        for (int i = 0; i < 10; i++) {
            set.put("Little" + i);
        }
        assertTrue(set.equals(set3));
    }

    @Test
    void testEqualsSetNot() {
        assertFalse(set3.equals(set4));
    }

    @Test
    void testSpeed() {      // на 10000 за 16 миллисекунд!?
        Random random = new Random(0x9E3779B97F4A7C15L);
        for (int i = 0; i < 10000; i++) {
            set1.put("value_" + random.nextInt(Integer.MAX_VALUE));
        }
    }

    @Test
    void testSpeedOnFullSize() {      // на 20000 за 88 миллисекунд!!!!
        Random random = new Random(0x9E3779B97F4A7C15L);
        for (int i = 0; i < 20000; i++) {
            set1.put("value_" + random.nextInt(Integer.MAX_VALUE));
        }
    }

    @Test
    void testCartesianMultiply() {
        PowerSet result = PowerSet_2.cartesianMultiply(set3, set4);
        assertEquals(1000, result.size());
    }

    @Test
    void testCartesianWithEmpty() {
        PowerSet result = PowerSet_2.cartesianMultiply(set1, set4);
        assertEquals(0, result.size());
        assertTrue(result.equals(new PowerSet()));
    }

    @Test
    void testMultyPulty() {
        ArrayList<PowerSet> sets = new ArrayList<PowerSet>();
        sets.add(set1);
        sets.add(set2);
        sets.add(set3);
        PowerSet result = PowerSet_2.multiIntersect(sets);
        assertTrue(result.equals(new PowerSet()));
    }

    @Test
    void testBag() {
        HashMap<String, Integer> values = bag.getAll();
        assertEquals(2, values.get("Bag02"));
        assertEquals(2, values.get("Bag05"));
        assertEquals(2, values.get("Bag09"));
        assertEquals(1, values.get("Bag12"));
        assertEquals(1, values.get("Bag27"));
    }
}
