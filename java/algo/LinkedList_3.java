import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

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

}