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
        linkedList2.head = linkedList2.tail;

        Node stableNode = linkedList2.tail; // с чего начинается обход списка - с хвоста
        Node movingNode = stableNode.prev;  // перемещается относительно хвоста последняя из нетронутых
        Node tempNode = movingNode.prev;    // временный указатель на предпредпоследнюю, чтобы не потерять

        while (tempNode != null) {
            movingNode.next = null;
            movingNode.prev = stableNode;

            stableNode = stableNode.prev;
            movingNode = movingNode.prev;
            tempNode = tempNode.prev;
        }

        linkedList2.tail = movingNode;
        linkedList2.tail.next = null;       // хвост становится головой
        linkedList2.head.prev = null;

    }
}
