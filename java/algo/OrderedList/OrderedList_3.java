package OrderedList;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class OrderedList_3 {
    // Курс "Практика в программировании на АСД. Задание 7.
    // Задача 7. Добавьте тесты для добавления, удаления и поиска элемента по его значению.

    OrderedList<Integer> ol1;
    OrderedList<Integer> ol2;
    OrderedList<Integer> ol3;
    OrderedList<Integer> ol4;

    @BeforeEach
    void setUp() {
        ol1 = new OrderedList<Integer>(true);   // 0 значений
        ol2 = new OrderedList<Integer>(true);   // 1 значение
        ol3 = new OrderedList<Integer>(true);   // несколько
        ol4 = new OrderedList<Integer>(false);  // несколько

        ol2.add(8);

        ol3.add(11);
        ol3.add(13);
        ol3.add(10);
        ol3.add(1);
        ol3.add(11);

        ol4.add(1);
        ol4.add(2);
        ol4.add(4);
        ol4.add(5);
        ol4.add(3);
    }

    @Test
    void testAdd1() {
        assertNull(ol1.head);
        assertNull(ol1.tail);
        assertEquals(0, ol1.count());
        ol1.add(4);
        assertEquals(4, ol1.head.value);
        assertEquals(4, ol1.tail.value);
        assertEquals(1, ol1.count());
    }

    @Test
    void testAdd2() {
        assertEquals(8, ol2.head.value);
        assertEquals(8, ol2.tail.value);
        assertEquals(1, ol2.count());
        ol2.add(4);
        assertEquals(4, ol2.head.value);
        assertEquals(8, ol2.tail.value);
        assertEquals(2, ol2.count());
    }

    @Test
    void testAdd3() {
        assertEquals(1, ol3.head.value);
        assertEquals(13, ol3.tail.value);
        assertEquals(5, ol3.count());
        ol3.add(10);
        ol3.add(13);
        assertEquals(7, ol3.count());
        assertEquals(1, ol3.head.value);
        assertEquals(13, ol3.tail.value);
    }

    @Test
    void testAdd4() {
        assertEquals(5, ol4.head.value);
        assertEquals(1, ol4.tail.value);
        assertEquals(5, ol4.count());
        ol4.add(2);
        ol4.add(7);
        ol4.add(0);
        assertEquals(7, ol4.head.value);
        assertEquals(0, ol4.tail.value);
        assertEquals(8, ol4.count());
    }

    @Test
    void testFind1() {
        assertNull(ol1.find(10));
    }

    @Test
    void testFind2() {
        assertEquals(ol2.tail, ol2.find(8));
        assertNull(ol2.find(9));
    }

    @Test
    void testFind3() {
        assertEquals(ol3.head, ol3.find(1));
        assertEquals(ol3.tail, ol3.find(13));
    }

    @Test
    void testFind4() {
        assertEquals(ol4.head, ol4.find(5));
        assertEquals(ol4.tail, ol4.find(1));
    }

    @Test
    void testDelete1() {
        // какой сюда вписать assert? assertNothingHappened? с другой стороны, проверить delete() на пустом списке надо
        ol1.delete(0);
    }

    @Test
    void testDelete2() {
        assertEquals(8, ol2.head.value);
        ol2.delete(8);
        assertNull(ol2.head);
        assertNull(ol2.tail);
    }

    @Test
    void testDelete3() {
        ol3.delete(1);
        ol3.delete(1);
        ol3.delete(11);
        ol3.delete(11);
        assertEquals(10, ol3.head.value);
        assertEquals(13, ol3.tail.value);
        assertEquals(2, ol3.count());
    }

    @Test
    void testDelete4() {
        ol4.delete(1);
        ol4.delete(5);
        assertEquals(4, ol4.head.value);
        assertEquals(2, ol4.tail.value);
    }
}
