import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;


class LinkedListTest {

    private LinkedList ll;
    private LinkedList ll1;
    private LinkedList ll2;
    private LinkedList ll3;
    private Node node4;
    private Node node5;

    @BeforeEach
    void setUp() {
        Node node1 = new Node(5);
        Node node2 = new Node(2);
        Node node3 = new Node(7);
        node4 = new Node(10);
        node5 = new Node(5);
        Node node6 = new Node(0);

        ll = new LinkedList();
        for (int i = 0; i < 10; i++) {
            ll.addInTail(new Node(5));
        }

        ll1 = new LinkedList();
        ll1.addInTail(node1);
        ll1.addInTail(node2);
        ll1.addInTail(node3);
        ll1.addInTail(node4);
        ll1.addInTail(node5);
        ll1.addInTail(node6);

        ll2 = new LinkedList();

        ll3 = new LinkedList();
        ll3.addInTail(new Node(11));
    }

    @Test
    void testAddInTail1() {
        Node node = new Node(144);
        ll1.addInTail(node);
        assertEquals(144, ll1.tail.value);
        assertEquals(5, ll1.head.value);
    }

    @Test
    void testAddInTail2() {
        Node node = new Node(144);
        ll2.addInTail(node);
        assertEquals(144, ll2.tail.value);
        assertEquals(144, ll2.head.value);
    }

    @Test
    void testAddInTail3() {
        Node node = new Node(144);
        ll3.addInTail(node);
        assertEquals(144, ll3.tail.value);
        assertEquals(11, ll3.head.value);
    }

    @Test
    void testAddInTail() {
        Node node = new Node(144);
        ll.addInTail(node);
        assertEquals(144, ll.tail.value);
        assertEquals(5, ll.head.value);
    }

    @Test
    void testFind1() {
        Node node = ll1.find(5);
        assertEquals(ll1.head, node);
    }

    @Test
    void testFind2() {
        Node node = ll2.find(5);
        assertEquals(null, node);
    }

    // Курс "Практика в программировании на АСД. Задание 1.
    // Задача 1. Добавьте в класс LinkedList метод удаления одного узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1)
    @Test
    void testRemove1() {
        boolean removeResult = ll1.remove(5);
        assertEquals(true, removeResult);
        assertEquals(2, ll1.head.value);
        assertEquals(0, ll1.tail.value);
    }

    @Test
    void testRemove2() {
        boolean removeResult = ll2.remove(10);
        assertEquals(false, removeResult);
        assertEquals(null, ll2.head);
        assertEquals(null, ll2.tail);
    }

    @Test
    void testRemove3() {
        boolean removeResult = ll3.remove(11);
        assertEquals(true, removeResult);
        assertEquals(null, ll3.head);
        assertEquals(null, ll3.tail);
    }

    @Test
    void testRemove() {
        boolean removeResult = ll.remove(5);
        assertEquals(true, removeResult);
        assertEquals(5, ll.head.value);
        assertEquals(5, ll.tail.value);
    }

    // Задача 2. Добавьте в класс LinkedList метод удаления всех узлов по конкретному значению.
    // Нормальное решение. Оставить проверку головы на финал, и проверить сначала весь оставшийся список.
    // Сложность решения по времени: O(n) - в худшем случае (n одних и тех же значений) проверяется n-1 значений, а потом отдельно голова.
    // Сложность решения по пространству: О(1).
    @Test
    void testRemoveAll1() {
        ll1.removeAll(5);
        assertEquals(2, ll1.head.value);
        assertEquals(0, ll1.tail.value);
        assertEquals(0, node4.next.value);
    }

    @Test
    void testRemoveAll2() {
        ll2.removeAll(5);
        assertEquals(null, ll2.head);
        assertEquals(null, ll2.tail);
    }

    @Test
    void testRemoveAll3() {
        ll3.removeAll(11);
        assertEquals(null, ll3.head);
        assertEquals(null, ll3.tail);
    }

    @Test
    void testRemoveAll() {
        assertEquals(10, ll.count());
        ll.removeAll(5);
        assertEquals(null, ll.head);
        assertEquals(null, ll.tail);
        assertEquals(0, ll.count());
    }

    // Задача 3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка).
    // Сложность решения по времени: O(1). Просто задаются новые голова и хвост, а бесхозные узлы постепенно уберёт сборщик мусора.
    // Сложность решения по пространству: О(1).
    @Test
    void testClear1() {
        ll1.clear();
        assertEquals(null, ll1.head);
        assertEquals(null, ll1.tail);
    }

    @Test
    void testClear2() {
        ll2.clear();
        assertEquals(null, ll2.head);
        assertEquals(null, ll2.tail);
    }

    @Test
    void testClear3() {
        ll3.clear();
        assertEquals(null, ll3.head);
        assertEquals(null, ll3.tail);
    }

    @Test
    void testClear() {
        ll.clear();
        assertEquals(null, ll.head);
        assertEquals(null, ll.tail);
    }

    // Задача 4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается список/массив найденных узлов).
    // Сложность решения по времени: O(n). В худшем случае мы соберём все узлы в новый список.
    // Сложность решения по пространству: О(n). В худшем случае мы соберём все узлы в новый список.
    @Test
    void testFindAll1() {
        ArrayList<Node> listNode = ll1.findAll(5);
        assertEquals(2, listNode.size());
        listNode = ll1.findAll(7);
        assertEquals(1, listNode.size());
        listNode = ll1.findAll(11);
        assertEquals(0, listNode.size());
    }

    @Test
    void testFindAll2() {
        ArrayList<Node> listNode = ll2.findAll(5);
        assertEquals(0, listNode.size());
    }

    @Test
    void testFindAll3() {
        ArrayList<Node> listNode = ll3.findAll(11);
        assertEquals(1, listNode.size());
        listNode = ll3.findAll(12);
        assertEquals(0, listNode.size());
    }

    @Test
    void testFindAll() {
        ArrayList<Node> listNode = ll.findAll(5);
        assertEquals(10, listNode.size());
        listNode = ll.findAll(0);
        assertEquals(0, listNode.size());
    }

    // Задача 5. Добавьте в класс LinkedList метод вычисления длины списка.
    // Сложность решения по времени: O(n). В любом случае надо обойти весь список.
    // Сложность решения по пространству: О(1). На выходе одно целочисленное значение.
    @Test
    void testCount1() {
        assertEquals(6, ll1.count());
    }

    @Test
    void testCount2() {
        assertEquals(0, ll2.count());
    }

    @Test
    void testCount3() {
        assertEquals(1, ll3.count());
    }

    @Test
    void testCount() {
        assertEquals(10, ll.count());
    }

    @Test
    void testInsertAfter1() {
        ll1.insertAfter(node4, new Node(55));
        assertEquals(7, ll1.count());
        assertEquals(55, node4.next.value);
        assertEquals(node5, node4.next.next);
    }

    @Test
    void testInsertAfter2() {
        ll2.insertAfter(null, new Node(2));
        assertEquals(1, ll2.count());
        assertEquals(2, ll2.head.value);
        assertEquals(2, ll2.tail.value);
    }

    @Test
    void testInsertAfter3() {
        ll3.insertAfter(null, new Node(2));
        assertEquals(2, ll3.count());
        assertEquals(2, ll3.head.value);
        assertEquals(11, ll3.tail.value);
    }

}