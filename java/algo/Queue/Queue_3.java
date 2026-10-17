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
        assertFalse(queue2.isEmpty());
    }

    @Test
    void testEnqueue1() {
        assertTrue(queue1.isEmpty());
        queue1.enqueue(5);
        queue1.enqueue(5);
        assertFalse(queue1.isEmpty());
        assertEquals(2, queue1.size());
    }

    @Test
    void testEnqueue2() {
        assertFalse(queue2.isEmpty());
        assertEquals(3, queue2.size());
        queue2.enqueue(5);
        queue2.enqueue(5);
        assertEquals(5, queue2.size());
    }

    @Test
    void testDequeue1() {
        assertTrue(queue1.isEmpty());
        assertThrows(IllegalStateException.class, () -> queue1.dequeue());
    }

    @Test
    void testDequeue2() {
        assertEquals(1, queue2.dequeue());
        assertEquals(2, queue2.dequeue());
        assertEquals(3, queue2.dequeue());
        assertThrows(IllegalStateException.class, () -> queue2.dequeue());
    }


}
