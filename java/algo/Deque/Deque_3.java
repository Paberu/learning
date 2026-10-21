package Deque;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Deque_3 {
    // Курс "Практика в программировании на АСД. Задание 6.
    // Задача 3. Добавьте для каждого из четырёх вышеупомянутых методов тесты: проверяйте изменившуюся длину очереди
    // и наличие или отстутствие в ней добавляемого/удаляемого элемента.
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
        assertEquals(0, deque1.size());
        deque1.addFront(3);
        assertEquals(3, deque1.peekTail());
        assertEquals(1, deque1.size());
    }

    @Test
    void testAddFront2() {
        assertEquals(1, deque2.size());
        assertNotNull(deque2.peekFront());
        deque2.addFront(3);
        assertEquals(2, deque2.size());
        assertEquals(3, deque2.peekFront());
        assertEquals(1, deque2.peekTail());
    }

    @Test
    void testAddFront3() {
        assertEquals(3, deque3.size());
        assertNotNull(deque3.peekFront());
        deque3.addFront(1);
        assertEquals(4, deque3.size());
        assertEquals(1, deque3.peekFront());
        assertEquals(4, deque3.peekTail());
    }

    @Test
    void testAddFront() {
        assertEquals(4, deque.size());
        assertNotNull(deque.peekFront());
        deque.addFront("Hola!");
        assertEquals(5, deque.size());
        assertEquals("Hola!", deque.peekFront());
        assertEquals("!", deque.peekTail());
    }

    @Test
    void testAddTail1() {
        assertEquals(0, deque1.size());
        assertNull(deque1.peekTail());
        deque1.addTail(3);
        assertEquals(1, deque1.size());
        assertEquals(3, deque1.peekFront());
    }

    @Test
    void testAddTail2() {
        assertEquals(1, deque2.size());
        assertNotNull(deque2.peekFront());
        deque2.addTail(3);
        assertEquals(2, deque2.size());
        assertEquals(3, deque2.peekTail());
        assertEquals(1, deque2.peekFront());
    }

    @Test
    void testAddTail3() {
        assertEquals(3, deque3.size());
        assertNotNull(deque3.peekFront());
        deque3.addTail(5);
        assertEquals(4, deque3.size());
        assertEquals(2, deque3.peekFront());
        assertEquals(5, deque3.peekTail());
    }

    @Test
    void testAddTail() {
        assertEquals(4, deque.size());
        assertNotNull(deque.peekFront());
        deque.addTail("Amigos!");
        assertEquals(5, deque.size());
        assertEquals("Hello", deque.peekFront());
        assertEquals("Amigos!", deque.peekTail());
    }

    @Test
    void testRemoveFront1() {
        assertEquals(0, deque1.size());
        assertNull(deque1.peekFront());
        assertNull(deque1.removeFront());
        assertEquals(0, deque1.size());
    }

    @Test
    void testRemoveFront2() {
        assertEquals(1, deque2.size());
        assertNotNull(deque2.peekFront());
        assertEquals(1, deque2.removeFront());
        assertEquals(0, deque2.size());
    }

    @Test
    void testRemoveFront3() {
        assertEquals(3, deque3.size());
        assertNotNull(deque3.peekFront());
        assertEquals(2, deque3.removeFront());
        assertEquals(2, deque3.size());
    }

    @Test
    void testRemoveFront() {
        assertEquals(4, deque.size());
        assertNotNull(deque.peekFront());
        assertEquals("Hello", deque.removeFront());
        assertEquals(3, deque.size());
    }

    @Test
    void testRemoveTail1() {
        assertEquals(0, deque1.size());
        assertNull(deque1.peekTail());
        assertNull(deque1.removeTail());
        assertEquals(0, deque1.size());
    }

    @Test
    void testRemoveTail2() {
        assertEquals(1, deque2.size());
        assertNotNull(deque2.peekFront());
        assertEquals(1, deque2.removeTail());
        assertEquals(0, deque2.size());
    }

    @Test
    void testRemoveTail3() {
        assertEquals(3, deque3.size());
        assertNotNull(deque3.peekFront());
        assertEquals(4, deque3.removeTail());
        assertEquals(2, deque3.size());
    }

    @Test
    void testRemoveTail() {
        assertEquals(4, deque.size());
        assertNotNull(deque.peekFront());
        assertEquals("!", deque.removeTail());
        assertEquals(3, deque.size());
    }
}
