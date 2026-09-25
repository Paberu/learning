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
    // Сложность решения по времени: O(n^2). Для каждого из n узлов надо полностью пробежать список из n узлов.
    // Сложность решения по пространству: О(1).
    public static void sortList(LinkedList2 linkedList2) {
        if (linkedList2.head == null || linkedList2.head == linkedList2.tail) {
            return;
        }

        Node currentNode = linkedList2.head.next; // допустим, первый узел уже на месте - переходим ко второму: его надо сдвигать, или он тоже на месте?
        while (currentNode != null) {
            Node sortedNode = currentNode.prev; // это ссылка на хвост уже отсортированной части, на первом проходе - голова списка
            Node nextNode = currentNode.next;   // после перестановок легко потерять следующий узел, можно в бесконечный цикл попасть (я попадал)

            while (sortedNode != null && sortedNode.value > currentNode.value) {
                sortedNode = sortedNode.prev;   // если sortedNode == null, значит currentNode станет новой головой, т.к. меньше всех уже отсортированных
            }                                   // либо остановится там, где можно вставить сразу после sortedNote

            if (sortedNode != currentNode.prev) { // если равен, он уже там, где надо
                currentNode.prev.next = currentNode.next;
                if (currentNode.next != null) {                 // вот здесь сложный момент, морально сложный:
                    currentNode.next.prev = currentNode.prev;   // если currentNode - не бывший хвост, то надо редактировать настройки следующего узла,
                } else {                                        // а иначе следующего узла нет, и надо просто заменить хвост;
                    linkedList2.tail = currentNode.prev;        // и как в такой ситуации навсегда избавиться от else?
                }                                               // нужен DummyNode из последней задачи

                // а дальше простая вставка или в самое начало или в середину списка
                if (sortedNode == null) {
                    currentNode.prev = null;
                    currentNode.next = linkedList2.head;
                    linkedList2.head.prev = currentNode;
                    linkedList2.head = currentNode;
                } else {
                    currentNode.prev = sortedNode;
                    currentNode.next = sortedNode.next;
                    sortedNode.next.prev = currentNode;
                    sortedNode.next = currentNode;
                }
            }
            currentNode = nextNode;
        }
    }

    // Задача 12. Добавьте метод, объединяющий два списка в третий.
    // Сложность решения по времени: O(n). Оба списка пробегаются один раз.
    // Сложность решения по пространству: O(n). Создаётся список размером в два предыдущих.
    public static LinkedList2 mergeTwoIntoOne(LinkedList2 firstList, LinkedList2 secondList) {
        sortList(firstList);
        sortList(secondList);
        LinkedList2 resultList = new LinkedList2();
        if (firstList.head == null) {   // если первый список пустой, вернуть копию второго
            return secondList.copy();
        }
        if (secondList.head == null) {  // если второй список пустой, вернуть копию первого
            return firstList.copy();
        }
        Node currentNode1 = firstList.head;
        Node currentNode2 = secondList.head;
        Node firstNode = null;          // надо определить, какая из двух голов (уже известно, что обе не null) будет головой результирующего списка.
        if (currentNode1.value > currentNode2.value) {
            firstNode = new Node(currentNode2.value);
            currentNode2 = currentNode2.next;
        } else {
            firstNode = new Node(currentNode1.value);
            currentNode1 = currentNode1.next;
        }
        resultList.addInTail(firstNode); // положено начало новому списку
        while (currentNode1 != null && currentNode2 != null) {
            if (currentNode2 == null || currentNode1.value >= currentNode2.value) {
                resultList.addInTail(new Node(currentNode1.value));
                currentNode1 = currentNode1.next;
            }
            if (currentNode1 == null || currentNode1.value < currentNode2.value) {
                resultList.addInTail(new Node(currentNode2.value));
                currentNode2 = currentNode2.next;
            }
        }

        return resultList;
    }

        // Задача 13. Добавьте фиктивный/пустой (dummy) узел.
        // Сложность решения по времени: .
        // Сложность решения по пространству: .

}
