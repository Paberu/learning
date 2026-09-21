import java.util.*;

public class LinkedList
{
    public Node head;
    public Node tail;

    public LinkedList()
    {
        head = null;
        tail = null;
    }

    public void addInTail(Node item) {
        if (this.head == null)
            this.head = item;
        else
            this.tail.next = item;
        this.tail = item;
    }

    public Node find(int value) {
        Node node = this.head;
        while (node != null) {
            if (node.value == value)
                return node;
            node = node.next;
        }
        return null;
    }

    // Курс "Практика в программировании на АСД. Задание 1.
    // Задача 1. Добавьте в класс LinkedList метод удаления одного узла по его значению.
    // Сложность решения по времени: O(n) - в худшем случае придётся пробежать весь список.
    // Сложность решения по пространству: О(1)
    public boolean remove(int _value) {
        // здесь будет ваш код удаления одного узла по заданному значению
        if (this.head == null) {
            return false;
        }

        if (this.head.value == _value) {
            this.head = this.head.next;
            if (this.head == null) {
                this.tail = null;
            }
            return true;
        } // отдельно удаление головы, ибо это не просто

        Node node = this.head;
        while (node != this.tail) {
            if (node.next.value == _value) {
                node.next = node.next.next; // и если node - это предпоследний узел, то node.next.next - это будет искомый null, то есть node.next будет равно null, а значит
                if (node.next == null) {    // next у текущей node станет равен null, а это признак того, что прежний хвост удалён, и текущая node теперь стала хвостом
                    this.tail = node;
                }
                return true;
            }
            node = node.next;
        }
        return false; // узел не нашли и не удалили
    }

    // Задача 2. Добавьте в класс LinkedList метод удаления всех узлов по конкретному значению.
    // Оставил халтурное решение, принятое вчера вечером. Осознание халтурности пришло при обдумывании сложности.
    // Сложность решения по времени: O(n^2) - в худшем случае (n одних и тех же значений) придётся пробежать весь список n раз, где n - размерность списка.
    // Сложность решения по пространству: О(1).
    public void removeAllDeprecated(int _value) {
        // здесь будет ваш код удаления всех узлов по заданному значению
        boolean removeFlag = true;
        while (removeFlag) {
            removeFlag = remove(_value);
        }
    }

    // Задача 2. Добавьте в класс LinkedList метод удаления всех узлов по конкретному значению.
    // Нормальное решение. Оставить проверку головы на финал, и проверить сначала весь оставшийся список.
    // Сложность решения по времени: O(n) - в худшем случае (n одних и тех же значений) проверяется n-1 значений, а потом отдельно голова.
    // Сложность решения по пространству: О(1).
    public void removeAll(int _value) {
        // здесь будет ваш код удаления всех узлов по заданному значению
        if (this.head == null) {
            return;
        }

        Node previousNode = this.head;
        Node node = this.head.next;
        while (node != null) {
            if (node.value == _value) {
                previousNode.next = node.next;
                if (previousNode.next == null) {
                    this.tail = previousNode;
                }
            }
            previousNode = previousNode.next;
            node = node.next;
        }
        // после проверки всего тела списка идёт проверка головы
        if (this.head.value == _value) {
            this.head = this.head.next; // это если в списке после удаления осталось что-то, кроме головы
            if (this.head == null) {
                this.tail = null;       // а здесь если ничего не осталось
            }
        }
    }

    public ArrayList<Node> findAll(int _value) {
        ArrayList<Node> nodes = new ArrayList<Node>();
        // здесь будет ваш код поиска всех узлов
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) {
                nodes.add(node);
            }
            node = node.next;
        }
        return nodes;
    }



    public void clear()
    {
        // здесь будет ваш код очистки всего списка
        this.head = null;
        this.tail = null;
    }

    public int count()
    {
        // здесь будет ваш код подсчёта количества элементов в списке
        int count = 0;
        Node node = this.head;
        while (node != null) {
            count++;
            node = node.next;
        }
        return count;
    }

    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        // здесь будет ваш код вставки узла после заданного

        // если _nodeAfter = null ,
        // добавьте новый элемент первым в списке
        if (_nodeAfter == null) {
            _nodeToInsert.next = this.head;
            this.head = _nodeToInsert;
            if (this.tail == null) {
                this.tail = _nodeToInsert;
            }
            return;
        }

        _nodeToInsert.next = _nodeAfter.next;
        _nodeAfter.next = _nodeToInsert;
    }

}

class Node
{
    public int value;
    public Node next;

    public Node(int _value)
    {
        value = _value;
        next = null;
    }
}