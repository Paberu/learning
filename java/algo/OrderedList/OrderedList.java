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

// Курс "Практика в программировании на АСД. Задание 7.
// Задача 1. Дополнительную опцию в конструкторе OrderedList, которая указывает, по возрастанию или по убыванию должны
// храниться элементы в массиве.
// Сложность решения по времени: O(1). Просто одна булева переменная.
// Сложность решения по пространству: О(1). Просто одна булева переменная.
public class OrderedList<T extends Comparable> {
    public Node<T> head, tail;
    private boolean _ascending;

    public OrderedList(boolean asc) {
        head = null;
        tail = null;
        _ascending = asc;
    }

    // Задача 2. Метод сравнения двух значений.
    // Сложность решения по времени: O(1). Элементы упорядоченного списка просто обязаны быть Comparable (иначе сам подход
    // не имеет смысла), поэтому можно пользоваться встроенной функцией compareTo. А другая встроенная функция понижает,
    // полученную разность с -N до -1, с N до 1, и лишь 0 всегда остаётся 0.
    // Сложность решения по пространству: О(1). Просто одна целочисленная переменная.

    // Задача 5. Мы в учебной задаче сделаем ограниченную реализацию: создадим единый класс-генерик, а в его методе
    // Compare() будем явно проверять, какой конкретно генерик-тип задан.
    // Сложность решения по времени: O(1). Я добавлю дополнительную проверку, на скорость решения она повлияет не сильно.
    // Сложность решения по пространству: О(1). Просто одна целочисленная переменная.
    // От себя хотел добавить, что эта добавка как будто не имеет смысла, т.к. в саму сигнатуру классы я внёс изменения,
    // без которых, имхо, задача не имеет смысла (а именно extends Comparable), а JVM сама решит проблему, как ей воплотить
    // compareTo() для конкретного класса. Теперь же строки "", "  " и "\t\t" будут считаться одинаковыми.
    public int compare(T v1, T v2) {
        if (v1 == null || v2 == null) {
            throw new IllegalArgumentException("Ни один из аргументов не может быть null");
        }
        if (v1 instanceof String && v2 instanceof String) {
            String strV1 = ((String) v1).strip();
            String strV2 = ((String) v2).strip();
            return Integer.signum(strV1.compareTo(strV2));
        }
        return Integer.signum(v1.compareTo(v2));
    }

    // Задача 3. Добавление нового элемента по значению.
    // Сложность решения по времени: O(n). Если элемент не меньше и не больше всех элементов списка, и ему место, например,
    // на предпредпоследнем, пардон, месте то придётся пробежать весь список. Индексов нет, двоичный поиск не прикрутить.
    // Сложность решения по пространству: О(1). Просто добавляется новый узел.
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

    // Задача 6. Переделайте функцию поиска с учётом признака упорядоченности и возможности раннего прерывания поиска,
    // если найден заведомо больший или меньший элемент, нежели искомый (то есть значение по сути не найдено).
    // Сложность решения по времени: O(n). При самом худшем варианте (ищем 100 в списке, упорядоченном от -99 до 99)
    // функция пробежит весь список, но прерывания работы так и не произойдёт.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public Node<T> find(T val) {
        if (head == tail) {  // 0 или 1 элемент
            if (head == null || compare(val, head.value) != 0) {
                return null;
            }
            return head;
        }
        Node<T> startNode = head;
        while (startNode != null) {
            int checkValue = compare(startNode.value, val);     // по задаче 6
            if ((_ascending && checkValue > 0) || (!_ascending && checkValue < 0))
                return null;
            if (checkValue == 0) {
                return startNode;
            }
            startNode = startNode.next;
        }
        return null;
    }

    // Задача 4. Удаление самого первого (одного) элемента по значению.
    // Сложность решения по времени: O(n). Если значение не в голове и не в хвосте списка, то придётся пробежать весь
    // список (в худшем случае, до предпоследнего узла, индексов-то снова нет).
    // Сложность решения по пространству: О(1). Просто удаляется узел.
    public void delete(T val) {
        if (head == null) return;
        if (head == tail && compare(head.value, val) == 0) {
            head = tail = null;
            return;
        }
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
            startNode = startNode.next;
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

    public boolean getAsc() {
        return _ascending;
    }
}