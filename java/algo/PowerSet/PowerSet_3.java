package PowerSet;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class PowerSet_3 {

    PowerSet set1;
    PowerSet set2;
    PowerSet set3;
    PowerSet set4;

    @BeforeEach
    void setUp() {
        set1 = new PowerSet();
        set2 = new PowerSet();
        set3 = new PowerSet();
        set4 = new PowerSet();

        set2.put("One and only");

        for (int i = 0; i < 10; i++) {
            set3.put("Little" + i);
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                set4.put("Big" + i + j);
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
}
