package LinkedList2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;


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
        assertEquals(null, node);
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

    // Задача 3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.

    // Задача 4. Добавьте в класс LinkedList2 метод удаления всех узлов по конкретному значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся. В крайнем случае (список из дубликатов) останет пустой список.

    // Задача 5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.

    // Задача 6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
    // Сложность решения по времени: O(1) - всегда в начало.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.

    // Задача 7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка).
    // Сложность решения по времени: O(1).
    // Сложность решения по пространству: О(1).

}
