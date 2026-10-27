package OrderedList;


import java.util.*;


class Node<T extends Comparable> {
    public T value;
    public Node<T> next, prev;

    public Node(T _value) {
        value = _value;
        next = null;
        prev = null;
    }
}

public class OrderedList<T extends Comparable> {
    public Node<T> head, tail;
    private boolean _ascending;

    public OrderedList(boolean asc) {
        head = null;
        tail = null;
        _ascending = asc;
    }

    public int compare(T v1, T v2) {
        if (v1 == null || v2 == null) {
            throw new IllegalArgumentException("Ни один из аргументов не может быть null");
        }
        return Integer.signum(v1.compareTo(v2));
    }

    public void add(T value) {
        Node node = new Node(value);
        if (head == null) {     // если первый в списке
            head = node;
            tail = node;
            return;
        }
        if ((_ascending && compare(value, head.value) <= 0) || (!_ascending && compare(value, head.value) >= 0)) {
            node.next = head;   // если надо вставить в начало
            head.prev = node;
            head = node;
            return;
        }
        if ((_ascending && compare(value, tail.value) >= 0) || (!_ascending && compare(value, tail.value) <= 0)) {
            node.prev = tail;   // если надо вставить в конец
            tail.next = node;
            tail = node;
            return;
        }
        Node<T> startNode = head;  // на все прочие случаи
        while (startNode != tail) {
            if ((_ascending && compare(value, startNode.value) > 0) || (!_ascending && compare(value, startNode.value) < 0)) {
                startNode = startNode.next;
            } else {
                node.next = startNode;
                node.prev = startNode.prev;
                startNode.prev.next = node;
                startNode.prev = node;
                return;
            }
        }
    }

    public Node<T> find(T val) {
        Node<T> startNode = head;
        while (startNode != tail) {
            if (compare(startNode.value, val) == 0) {
                return startNode;
            }
            startNode = startNode.next;
        }
        return null;
    }

    public void delete(T val) {
        if (compare(head.value, val) == 0) {    // удалить из головы
            head.next.prev = null;
            head = head.next;
            return;
        }
        if (compare(tail.value, val) == 0) {    // удалить из хвоста
            tail.prev.next = null;
            tail = tail.prev;
            return;
        }
        Node<T> startNode = head;               // прочие случаи
        while (startNode != tail) {
            if (compare(startNode.value, val) == 0) {
                startNode.next.prev = startNode.prev;
                startNode.prev.next = startNode.next;
                return;
            }
        }
    }

    public void clear(boolean asc) {
        _ascending = asc; // просто оставить head = null, tail == null даст утечку памяти
        Node startNode = head;
        while (startNode != null) {
            Node currentNode = startNode;
            startNode = startNode.next;
            currentNode.prev = null;
            currentNode.next = null;
        }
        head = null;
        tail = null;
    }

    public int count() {
        int count = 0;
        Node<T> node = head;
        while (node != null) {
            count++;
            node = node.next;
        }
        return count;
    }

    ArrayList<Node<T>> getAll() { // выдать все элементы упорядоченного списка в виде стандартного списка
        ArrayList<Node<T>> r = new ArrayList<Node<T>>();
        Node<T> node = head;
        while(node != null) {
            r.add(node);
            node = node.next;
        }
        return r;
    }
}