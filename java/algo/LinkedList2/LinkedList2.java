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
    public boolean remove(int _value)
    {
        // здесь будет ваш код удаления одного узла по заданному значению
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                if (node == this.head) {
                    this.head = this.head.next;
                    this.head.prev = null;
                    return true;
                }
                if (node == this.tail) {
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
        return false; // если узел был удалён
    }

    // Задача 4. Добавьте в класс LinkedList2 метод удаления всех узлов по конкретному значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся. В крайнем случае (список из дубликатов) останет пустой список.
    public void removeAll(int _value) {
        // здесь будет ваш код удаления всех узлов по заданному значению
        Node node
    }

    public void clear()
    {
        // здесь будет ваш код очистки всего списка
    }

    public int count()
    {
        return 0; // здесь будет ваш код подсчёта количества элементов в списке
    }

    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        // здесь будет ваш код вставки узла после заданного узла

        // если _nodeAfter = null
        // добавьте новый элемент первым в списке
    }
}

class Node
{
    public int value;
    public Node next;
    public Node prev;

    public Node(int _value)
    {
        value = _value;
        next = null;
        prev = null;
    }
}