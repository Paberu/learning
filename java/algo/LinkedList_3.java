import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;


class LinkedListTest {

    private LinkedList ll1;
    private LinkedList ll2;
    private LinkedList ll3;

    @BeforeEach
    void setUp() {
        Node node1 = new Node(5);
        Node node2 = new Node(2);
        Node node3 = new Node(7);
        Node node4 = new Node(10);
        Node node5 = new Node(5);
        Node node6 = new Node(0);

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
    void testAddInTail() {
        Node node = new Node(144);
        ll1.addInTail(node);
        assertEquals(144, ll1.tail.value);

        node = new Node(144);
        ll2.addInTail(node);
        assertEquals(144, ll2.tail.value);

        node = new Node(144);
        ll3.addInTail(node);
        assertEquals(144, ll3.tail.value);
    }

    @Test
    void testFind() {
        Node node = ll1.find(5);
        assertEquals(ll1.head, node);

        node = ll2.find(5);
        assertEquals(null, node);
    }

    @Test
    void testFindAll() {
        ArrayList<Node> listNode = ll1.findAll(5);
        assertEquals(2, listNode.size());

        listNode = ll3.findAll(5);
        assertEquals(0, listNode.size());
    }

    @Test
    void testRemove() {
        boolean removeResult = ll1.remove(5);
        assertEquals(true, removeResult);
        assertEquals(2, ll1.head.value);

        removeResult = ll2.remove(10);
        assertEquals(false, removeResult);

        removeResult = ll3.remove(11);
        assertEquals(true, removeResult);
        assertEquals(null, ll3.head);
        assertEquals(null, ll3.tail);
    }

    @Test
    void testClear() {
        ll1.clear();
        assertEquals(null, ll1.head);
        assertEquals(null, ll1.tail);
    }

    @Test
    void testCount() {
        assertEquals(6, ll1.count());
        assertEquals(0, ll2.count());
        assertEquals(1, ll3.count());
    }
}