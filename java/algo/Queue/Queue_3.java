package Queue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Queue_3 {
    Queue queue1;
    Queue queue2;

    @BeforeEach
    void setUp() {
        queue1 = new Queue();
        queue2 = new Queue();
        queue2.enqueue(1);
        queue2.enqueue(2);
        queue2.enqueue(3);
    }

    @Test
    void testSize1() {
        assertEquals(0, queue1.size());
    }

    @Test
    void testSize2() {
        assertEquals(3, queue2.size());
    }

    @Test
    void testEmpty1() {
        assertTrue(queue1.isEmpty());
    }

    @Test
    void testEmpty2() {
        assertFalse(queue1.isEmpty());
    }


}
