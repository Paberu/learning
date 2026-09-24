package LinkedList2;

public class LinkedList2_2 {
    // Курс "Практика в программировании на АСД. Задание 2.
    // Задача 9. Добавьте метод, который "переворачивает" порядок элементов в связном списке, меняя его на противоположный.
    // Упрощенный вариант решения: через создание временного списка.
    // Сложность решения по времени: O(n) - всегда надо обойти весь список.
    // Сложность решения по пространству: О(n) - всегда создаётся новый список.
    public static LinkedList2 reversedList(LinkedList2 linkedList2) {
        if (linkedList2.head == null || linkedList2.head == linkedList2.tail) {
            return linkedList2;
        }
        LinkedList2 reversedLL = new LinkedList2();
        Node node = linkedList2.tail;
        while (node != null) {
            reversedLL.addInTail(new Node(node.value));
            node = node.prev;
        }
        return reversedLL;
    }

    // Задача 9. Добавьте метод, который "переворачивает" порядок элементов в связном списке, меняя его на противоположный
    // Сложность решения по времени: O(n) - всегда надо обойти весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.

    public static void reverseList(LinkedList2 linkedList2) {
        if (linkedList2.head == null || linkedList2.head == linkedList2.tail) {
            return;
        }
        Node exHead = linkedList2.head;     // сохраняется указатель на прежний головной узел
        linkedList2.head = linkedList2.tail;// хвост становится головой...

        Node stableNode = linkedList2.tail; // с чего начинается обход списка - с хвоста
        Node movingNode = stableNode.prev;  // перемещается относительно хвоста последняя из нетронутых

        while (movingNode != null) {
            Node tempNode = movingNode.prev;    // временный указатель на предпредпоследнюю, чтобы не потерять
            movingNode.prev = stableNode;
            stableNode.next = movingNode;

            stableNode = movingNode;
            movingNode = tempNode;
        }

        linkedList2.tail = exHead;          //... а голова хвостом
        linkedList2.tail.next = null;
        linkedList2.head.prev = null;
    }
        // Задача 10. Добавьте булев метод, который сообщает, имеются ли циклы (замкнутые на себя по кругу) внутри списка.
        // Сложность решения по времени: .
        // Сложность решения по пространству: .

        // Задача 11. Добавьте метод, сортирующий список.
        // Сложность решения по времени: .
        // Сложность решения по пространству: .
    public static void sortList(LinkedList2 linkedList2) {
        if (linkedList2.head == null || linkedList2.head == linkedList2.tail) {
            return;
        }
        Node exHead = linkedList2.head;
        Node exTail = linkedList2.tail;

        Node movingNode = linkedList2.tail;
        boolean moved = false;
        Node startNode = linkedList2.head;

        while (movingNode != exTail) {
            if (movingNode.value < startNode.value) {
                movingNode.next = startNode;
                startNode.prev = movingNode;
                if (startNode == exHead) {
                    linkedList2.head = movingNode;
                }
                linkedList2.tail = movingNode.prev;
                movingNode.prev = null;
            }
        }
    }

        // Задача 12. Добавьте метод, объединяющий два списка в третий.
        // Сложность решения по времени: .
        // Сложность решения по пространству: .

        // Задача 13. Добавьте фиктивный/пустой (dummy) узел.
        // Сложность решения по времени: .
        // Сложность решения по пространству: .

}
