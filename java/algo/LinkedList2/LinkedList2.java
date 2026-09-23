package LinkedList2;


import java.util.ArrayList;

public class LinkedList2 {
    public Node head;
    public Node tail;

    public LinkedList2() {
        head = null;
        tail = null;
    }

    public void addInTail(Node _item) {
        if (head == null) {
            this.head = _item;
            this.head.next = null;
            this.head.prev = null;
        } else {
            this.tail.next = _item;
            _item.prev = tail;
        }
        this.tail = _item;
    }

    // Курс "Практика в программировании на АСД. Задание 2.
    // Задача 1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public Node find(int _value) {
        // здесь будет ваш код поиска
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                return node;
            }
            node = node.next;
        }
        return null;
    }

    // Задача 2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(n) - в худшем случае получится копия изначального списка (если список состоит из одних лишь дубликатов).
    public ArrayList<Node> findAll(int _value)
    {
        ArrayList<Node> nodes = new ArrayList<Node>();
        // здесь будет ваш код поиска всех узлов по заданному значению
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                nodes.add(node);
            }
            node = node.next;
        }
        return nodes;
    }

    // Задача 3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public boolean remove(int _value) {
        // здесь будет ваш код удаления одного узла по заданному значению
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                if (this.head == this.tail) { // граничный случай: удалить единственный узел, он же голова, он же хвост.
                    this.head = null;
                    this.tail = null;
                    return true;
                }
                if (node == this.head) {    // граничный случай: удалить голову
                    this.head = this.head.next;
                    this.head.prev = null;
                    return true;
                }
                if (node == this.tail) {    // граничный случай: удалить хвост
                    this.tail = this.tail.prev;
                    this.tail.next = null;
                    return true;
                }
                node.prev.next = node.next;
                node.next.prev = node.prev;
                return true;
            }
            node = node.next;
        }
        return false; // если узел не был удалён
    }

    // Задача 4. Добавьте в класс LinkedList2 метод удаления всех узлов по конкретному значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся. В крайнем случае (список из дубликатов) останет пустой список.
    public void removeAll(int _value) {
        // здесь будет ваш код удаления всех узлов по заданному значению
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                if (node == this.head) {
                    this.head = this.head.next;
                    this.head.prev = null;
                } else if (node == this.tail) {
                    this.tail = this.tail.prev;
                    this.tail.next = null;
                } else {
                    if (this.head == this.tail) { // граничный случай: удалить единственный узел, он же голова, он же хвост.
                        this.head = null;
                        this.tail = null;
                    }
                    node.prev.next = node.next;
                    node.next.prev = node.prev;
                }
            }
            node = node.next;
        }
    }
    // Задача 5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        // здесь будет ваш код вставки узла после заданного узла
        if (_nodeAfter == null) {
            if (this.head == null) {
                this.addInTail(_nodeToInsert);
                return;
            }
            this.head.prev = _nodeToInsert;
            _nodeToInsert.next = this.head;
            this.head = _nodeToInsert;
            return;
        } // если _nodeAfter = null
        // добавьте новый элемент первым в списке

        if (_nodeAfter == this.tail) {
            this.addInTail(_nodeToInsert);
            return;
        } // второй крайний случай - добавление в хвост - уже задан по умолчанию предварительно.

        Node exAfterNext = _nodeAfter.next;
        _nodeAfter.next = _nodeToInsert;
        _nodeToInsert.next = exAfterNext;
        exAfterNext.prev = _nodeToInsert;
        _nodeToInsert.prev = _nodeAfter;
    }
    // Задача 6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
    // Сложность решения по времени: O(1) - всегда в начало.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public void insertFirst(Node _nodeToInsert) {
        insertAfter(null, _nodeToInsert);
    }

    // Задача 7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка).
    // Сложность решения по времени: O(1).
    // Сложность решения по пространству: О(1).
    public void clear() {
        // здесь будет ваш код очистки всего списка
        this.head = null;
        this.tail = null;
    }

    public int count() {
        int size = 0;
        Node node = this.head;
        while (node != null) {
            size ++;
            node = node.next;
        }
        return size; // здесь будет ваш код подсчёта количества элементов в списке
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