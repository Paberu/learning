package Queue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Queue_3 {
    Queue queue1;
    Queue queue2;
    Queue queue3;

    @BeforeEach
    void setUp() {
        queue1 = new Queue();
        queue2 = new Queue();
        queue2.enqueue(1);
        queue2.enqueue(2);
        queue2.enqueue(3);
        queue3 = new Queue();
        queue3.enqueue(10);
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
    void testSize3() {
        assertEquals(1, queue3.size());
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
    void testEmpty3() {
        assertFalse(queue3.isEmpty());
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
    void testEnqueue3() {
        assertFalse(queue3.isEmpty());
        assertEquals(1, queue3.size());
        queue3.enqueue(5);
        queue3.enqueue(5);
        assertEquals(3, queue3.size());
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

    @Test
    void testDequeue3() {
        assertEquals(10, queue3.dequeue());
        assertThrows(IllegalStateException.class, () -> queue3.dequeue());
    }

    @Test
    void testRotate1() {
        assertTrue(queue1.isEmpty());
        assertThrows(IllegalStateException.class, () -> Queue_2.rotate(queue1, 4));
    }

    @Test
    void testRotate2() {
        Queue_2.rotate(queue2, 4);
        assertEquals(2, queue2.dequeue());
        assertEquals(3, queue2.dequeue());
        assertEquals(1, queue2.dequeue());
        assertThrows(IllegalStateException.class, () -> queue2.dequeue());
    }

    @Test
    void testRotate3() {
        Queue_2.rotate(queue3, 4);
        assertEquals(10, queue3.dequeue());
        assertThrows(IllegalStateException.class, () -> queue3.dequeue());
    }

    @Test
    void testReverse1() {
        assertTrue(queue1.isEmpty());
        Queue_2.reverse(queue1);
        assertTrue(queue1.isEmpty());
    }

    @Test
    void testReverse2() {
        Queue_2.reverse(queue2);
        assertEquals(3, queue2.dequeue());
        assertEquals(2, queue2.dequeue());
        assertEquals(1, queue2.dequeue());
        assertThrows(IllegalStateException.class, () -> queue2.dequeue());
    }

    @Test
    void testReverse3() {
        Queue_2.reverse(queue3);
        assertEquals(10, queue3.dequeue());
        assertThrows(IllegalStateException.class, () -> queue3.dequeue());
    }

    @Test
    void testStackedQueue() {
        StackedQueue queue = new StackedQueue();
        queue.enqueue(14);
        queue.enqueue(10);
        queue.enqueue(5);
        assertEquals(14, queue.dequeue());
        assertEquals(10, queue.dequeue());
        assertEquals(5, queue.dequeue());
    }

}
