package LinkedList2;

import LinkedList.LinkedList;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;


public class LinkedList2_3 {

    private LinkedList2 ll;
    private LinkedList2 ll1;
    private LinkedList2 ll2;
    private LinkedList2 ll3;
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

        ll = new LinkedList2();
        for (int i = 0; i < 10; i++) {
            ll.addInTail(new Node(5));
        }

        ll1 = new LinkedList2();
        ll1.addInTail(node1);
        ll1.addInTail(node2);
        ll1.addInTail(node3);
        ll1.addInTail(node4);
        ll1.addInTail(node5);
        ll1.addInTail(node6);

        ll2 = new LinkedList2();

        ll3 = new LinkedList2();
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

    // Курс "Практика в программировании на АСД. Задание 2.
    // Задача 1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    @Test
    void testFind1() {
        Node node = ll1.find(10);
        assertEquals(node4, node);
    }

    @Test
    void testFind2() {
        Node node = ll2.find(5);
        assertNull(node);
    }

    @Test
    void testFind3() {
        Node node = ll3.find(11);
        assertEquals(ll3.head, node);
    }

    @Test
    void testFind() {
        Node node = ll.find(5);
        assertEquals(ll.head, node);
    }

    // Задача 2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(n) - в худшем случае получится копия изначального списка (если список состоит из одних лишь дубликатов).
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

    // Задача 3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    @Test
    void testRemove1() {
        boolean removeResult = ll1.remove(5);
        assertTrue(removeResult);
        assertEquals(2, ll1.head.value);
        assertEquals(0, ll1.tail.value);
    }

    @Test
    void testRemove2() {
        boolean removeResult = ll2.remove(10);
        assertFalse(removeResult);
        assertNull(ll2.head);
        assertNull(ll2.tail);
    }

    @Test
    void testRemove3() {
        boolean removeResult = ll3.remove(11);
        assertTrue(removeResult);
        assertNull(ll3.head);
        assertNull(ll3.tail);
    }

    @Test
    void testRemove() {
        boolean removeResult = ll.remove(5);
        assertTrue(removeResult);
        assertEquals(5, ll.head.value);
        assertEquals(5, ll.tail.value);
    }

    @Test
    void testRemoveTail() {
        LinkedList2 tempLL = new LinkedList2();
        Node head = new Node(1);
        Node tail = new Node(2);
        tempLL.addInTail(head);
        tempLL.addInTail(tail);
        boolean removeResult = tempLL.remove(2);
        assertTrue(removeResult);
        assertEquals(head, tempLL.head);
        assertEquals(head, tempLL.tail);
    }

    // Задача 4. Добавьте в класс LinkedList2 метод удаления всех узлов по конкретному значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся. В крайнем случае (список из дубликатов) останет пустой список.
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
        assertNull(ll2.head);
        assertNull(ll2.tail);
    }

    @Test
    void testRemoveAll3() {
        ll3.removeAll(11);
        assertNull(ll3.head);
        assertNull(ll3.tail);
    }

    @Test
    void testRemoveAll() {
        assertEquals(10, ll.count());
        ll.removeAll(5);
        assertNull(ll.head);
        assertNull(ll.tail);
        assertEquals(0, ll.count());
    }

    @Test
    void testRemoveAllTail() {
        LinkedList2 tempLL = new LinkedList2();
        Node head = new Node(1);
        Node tail = new Node(2);
        tempLL.addInTail(head);
        tempLL.addInTail(tail);
        tempLL.addInTail(new Node(2));
        tempLL.addInTail(new Node(2));
        tempLL.addInTail(new Node(2));
        tempLL.removeAll(2);
        assertEquals(head, tempLL.head);
        assertEquals(head, tempLL.tail);
    }

    // Задача 5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    @Test
    void testInsertAfter1() {
        Node node = new Node(55);
        ll1.insertAfter(node4, node);
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

    @Test
    void testInsertAfter() {
        ll.insertAfter(null, new Node(2));
        assertEquals(11, ll.count());
        assertEquals(2, ll.head.value);
        assertEquals(5, ll.tail.value);
    }

    @Test
    void testInsertAfterFail1() {
        LinkedList2 tempLL = new LinkedList2();
        Node tmpNode1 = new Node(3);
        tempLL.addInTail(tmpNode1);
        Node tmpNode2 = new Node(4);
        tempLL.insertAfter(tmpNode1, tmpNode2);
        assertEquals(tmpNode1, tempLL.head);
        assertEquals(tmpNode2, tempLL.tail);

    }
    // Задача 6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
    // Сложность решения по времени: O(1) - всегда в начало.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    @Test
    void testInsertFirst1() {
        Node node = new Node(55);
        ll1.insertFirst(node);
        assertEquals(7, ll1.count());
        assertEquals(55, ll1.head.value);
        assertEquals(5, node.next.value);
    }

    @Test
    void testInsertFirst2() {
        ll2.insertFirst(new Node(2));
        assertEquals(1, ll2.count());
        assertEquals(2, ll2.head.value);
        assertEquals(2, ll2.tail.value);
    }

    @Test
    void testInsertFirst3() {
        ll3.insertFirst(new Node(2));
        assertEquals(2, ll3.count());
        assertEquals(2, ll3.head.value);
        assertEquals(11, ll3.tail.value);
    }

    @Test
    void testInsertFirst() {
        ll.insertFirst(new Node(2));
        assertEquals(11, ll.count());
        assertEquals(2, ll.head.value);
        assertEquals(5, ll.tail.value);
    }

    // Задача 7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка).
    // Сложность решения по времени: O(1).
    // Сложность решения по пространству: О(1).
    @Test
    void testClear1() {
        ll1.clear();
        assertNull(ll1.head);
        assertNull(ll1.tail);
    }

    @Test
    void testClear2() {
        ll2.clear();
        assertNull(ll2.head);
        assertNull(ll2.tail);
    }

    @Test
    void testClear3() {
        ll3.clear();
        assertNull(ll3.head);
        assertNull(ll3.tail);
    }

    @Test
    void testClear() {
        ll.clear();
        assertNull(ll.head);
        assertNull(ll.tail);
    }

    // Задача 9. Добавьте метод, который "переворачивает" порядок элементов в связном списке, меняя его на противоположный.
    // Упрощенный вариант решения: через создание временного списка.
    // Сложность решения по времени: O(n) - всегда надо обойти весь список.
    // Сложность решения по пространству: О(n) - всегда создаётся новый список.
    @Test
    void testReversedList1(){
        LinkedList2 tempLL = LinkedList2_2.reversedList(ll1);
        assertEquals(0, tempLL.head.value);
        assertEquals(5, tempLL.tail.value);
    }

    @Test
    void testReversedList2(){
        LinkedList2 tempLL = LinkedList2_2.reversedList(ll2);
        assertNull(tempLL.head);
        assertNull(tempLL.tail);
    }

    @Test
    void testReversedList3(){
        LinkedList2 tempLL = LinkedList2_2.reversedList(ll3);
        assertEquals(11, tempLL.head.value);
        assertEquals(11, tempLL.tail.value);
    }

    @Test
    void testReversedList(){
        LinkedList2 tempLL = LinkedList2_2.reversedList(ll);
        assertEquals(5, tempLL.head.value);
        assertEquals(5, tempLL.tail.value);
    }

    @Test
    void testReversedListFailed() {
        LinkedList2 llFailed = new LinkedList2();
        for (int i = 0; i < 10; i++) {
            llFailed.addInTail(new Node(i));
        }
        LinkedList2 tempLL = LinkedList2_2.reversedList(llFailed);
        Node node = tempLL.head;
        for (int i = 9; i >= 0; i--) {
            assertEquals(i, node.value);
            node = node.next;
        }
    }
}
