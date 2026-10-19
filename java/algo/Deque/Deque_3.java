package Deque;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Deque_3 {
    Deque<Integer> deque1;
    Deque<Integer> deque2;
    Deque<Integer> deque3;
    Deque<String> deque;

    @BeforeEach
    void setUp() {
        deque1 = new Deque<Integer>();
        deque2 = new Deque<Integer>();
        deque3 = new Deque<Integer>();
        deque = new Deque<String>();

        deque2.addTail(1);

        deque3.addTail(2);
        deque3.addTail(3);
        deque3.addTail(4);

        deque.addTail("Hello");
        deque.addTail(",");
        deque.addTail("world");
        deque.addTail("!");
    }

    @Test
    void testAddFront1() {
        assertNull(deque1.peekFront());
        deque1.addFront(3);
        assertEquals(3, deque1.peekTail());
    }

    @Test
    void testAddFront2() {
        assertNotNull(deque2.peekFront());
        deque2.addFront(3);
        assertEquals(3, deque2.peekFront());
        assertEquals(1, deque2.peekTail());
    }

    @Test
    void testAddFront3() {
        assertNotNull(deque3.peekFront());
        deque3.addFront(1);
        assertEquals(1, deque3.peekFront());
        assertEquals(4, deque3.peekTail());
    }

    @Test
    void testAddFront() {
        assertNotNull(deque.peekFront());
        deque.addFront("Hola!");
        assertEquals("Hola!", deque.peekFront());
        assertEquals("!", deque.peekTail());
    }

    @Test
    void testAddTail1() {
        assertNull(deque1.peekTail());
        deque1.addTail(3);
        assertEquals(3, deque1.peekFront());
    }

    @Test
    void testAddTail2() {
        assertNotNull(deque2.peekFront());
        deque2.addTail(3);
        assertEquals(3, deque2.peekTail());
        assertEquals(1, deque2.peekFront());
    }

    @Test
    void testAddTail3() {
        assertNotNull(deque3.peekFront());
        deque3.addTail(5);
        assertEquals(2, deque3.peekFront());
        assertEquals(5, deque3.peekTail());
    }

    @Test
    void testAddTail() {
        assertNotNull(deque.peekFront());
        deque.addTail("Amigos!");
        assertEquals("Hello", deque.peekFront());
        assertEquals("Amigos!", deque.peekTail());
    }
}
