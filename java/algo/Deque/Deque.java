package Deque;
import java.util.*;

public class Deque<T> {
    private Node<T> head;
    private Node<T> tail;
    private int size;
    private TreeMap<T, Integer> mins = new TreeMap<>();

    // Курс "Практика в программировании на АСД. Задание 6.
    // Задача 1. Реализуйте упомянутые выше класс Deque и соответствующие методы.
    public Deque() {
        head = new DummyNode<T>();
        tail = new DummyNode<T>();
        tail.prev = head;
        head.next = tail;
        size = 0;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    // Задача 2. Как можно понизить (выровнять) сложность addHead/removeHead и addTail/removeTail, с помощью какого ранее изученного типа данных?
    // Однозначно, моя one-love для стеков и очередей, ранее мною непонятый тип данных - двунаправленный связный список.
    // Сложность по времени всех 4 функций всегда O(1), мы всегда имеем доступ к обеим сторонам очереди, добавление/удаление всегда
    // стоит 1, независимо от размера очереди и итогового типа у item. Но есть и минусы - в таком классе нужны добавочные
    // хранилища для выдачи минимальных значений, для поиска среднего арифметического и т.д.
    public void addFront(T item) {
        Node<T> node = new Node<>(item);
        node.next = head.next;
        node.prev = head;

        head.next.prev = node;
        head.next = node;
        mins.merge(item, 1, Integer::sum);
        size++;
    }

    public void addTail(T item) {
        Node<T> node = new Node<>(item);
        node.prev = tail.prev;
        node.next = tail;

        tail.prev.next = node;
        tail.prev = node;
        mins.merge(item, 1, Integer::sum);
        size++;
    }

    public T removeFront() {
        if (isEmpty()) return null;
        Node<T> node = head.next;
        node.next.prev = head;
        head.next = node.next;
        node.prev = null;
        node.next = null;
        removeMin(node.value);
        size--;
        return node.value;
    }

    public T removeTail() {
        if (isEmpty()) return null;
        Node<T> node = tail.prev;
        node.prev.next = tail;
        tail.prev = node.prev;
        node.prev = null;
        node.next = null;
        removeMin(node.value);
        size--;
        return node.value;
    }

    public T min() {
        if (isEmpty()) return null;
        return mins.firstKey();
    }

    public T peekFront() {
        if (isEmpty()) return null;
        return head.next.value;
    }

    public T peekTail() {
        if (isEmpty()) return null;
        return tail.prev.value;
    }

    private void removeMin(T value) {
        int minimalCount = mins.get(value);
        if (minimalCount == 1) {
            mins.remove(value);
            return;
        }
        mins.put(value, minimalCount-1);
    }
}

class Node<T> {
    T value;
    Node<T> next;
    Node<T> prev;

    public Node(T value) {
        this.value = value;
        next = null;
        prev = null;
    }
}

class DummyNode<T> extends Node<T> {
    public DummyNode() {
        super(null);
    }
}