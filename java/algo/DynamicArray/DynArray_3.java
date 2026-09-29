package DynamicArray;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class DynArray_3 {
    DynArray<Integer> dynArray;

    @BeforeEach
    void setUp(){
        dynArray = new DynArray<Integer>(Integer.class);
        for (int i = 0; i < 14; i++) {
            dynArray.append(i*2);
        }
    }

    @Test
    void testInsertLight() {
        assertEquals(16, dynArray.capacity);
        assertEquals(14, dynArray.count);
        dynArray.append(17);
        assertEquals(16, dynArray.capacity);
        assertEquals(15, dynArray.count);
    }

    @Test
    void testInsertHeavy() {
        assertEquals(16, dynArray.capacity);
        assertEquals(14, dynArray.count);
        dynArray.append(17);
        dynArray.append(19);
        assertEquals(16, dynArray.capacity);
        assertEquals(16, dynArray.count);
        dynArray.append(21);
        assertEquals(32, dynArray.capacity);
        assertEquals(17, dynArray.count);
    }
}
