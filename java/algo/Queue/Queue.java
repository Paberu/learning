package Queue;

public class Queue {
    private Node head;
    private Node tail;
    private int size;

    public Queue() {
        this.head = new DummyNode();
        this.tail = new DummyNode();
        this.tail.prev = this.head;
        this.head.next = this.tail;
        this.size = 0;
    }

    public int size() {
        return this.size;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public void enqueue(int value) {
        Node node = new Node(value);
        node.prev = this.tail.prev;
        node.next = this.tail;

        this.tail.prev.next = node;
        this.tail.prev = node;

        this.size++;
    }

    public int dequeue() {
        if (isEmpty()) throw new IllegalStateException("Нельзя достать что-то из пустой очереди.");
        Node first = this.head.next;
        first.next.prev = this.head;
        this.head.next = first.next;
        this.size--;
        return first.value;
    }
}

class Node {
    public int value;
    public Node next;
    public Node prev;

    public Node(int _value) {
        value = _value;
        next = null;
        prev = null;
    }
}

class DummyNode extends Node {
    public DummyNode() {
        super(0);
    }
}