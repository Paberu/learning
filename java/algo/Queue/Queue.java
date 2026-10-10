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

    // Курс "Практика в программировании на АСД. Задание 5.
    // Задача 1. В классе Queue нам понадобятся три метода: size() (количество элементов в очереди), enqueue(item).
    // Сложность решения по времени: O(1). Я сделал отдельный параметр класса, не надо пробегать всю очередь.
    // Сложность решения по пространству: О(1). Для очередей любого размера это всегда одна переменная типа int.
    public int size() {
        return this.size;
    }

    // Вспомогательная функция, коих навалом во встроенных в JDK классах.
    public boolean isEmpty() {
        return this.size == 0;
    }

    // Задача 2. Оцените меру сложности для операций enqueue() (добавление) и dequeue() (удаление) в данной реализации.
    // Сложность решения по времени: O(1). Реализовал через связный список с использованием DummyNode (зря я их что ли реализовывал).
    // Сложность решения по пространству: О(1). Создаётся один новый узел, который и добавляется в очередь.
    public void enqueue(int value) {
        Node node = new Node(value);
        node.prev = this.tail.prev;
        node.next = this.tail;

        this.tail.prev.next = node;
        this.tail.prev = node;

        this.size++;
    }

    // Задача 2. Оцените меру сложности для операций enqueue() (добавление) и dequeue() (удаление) в данной реализации.
    // Сложность решения по времени: O(1). Связный список позволяет не сдвигать весь массив данных на единицу, а наличие DummyNode не проверять пограничные случаи.
    // Сложность решения по пространству: О(1). Создаётся один новый указатель на уже существующий узел.
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