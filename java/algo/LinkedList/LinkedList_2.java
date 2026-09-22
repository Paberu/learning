package LinkedList;


class LinkedListUtils {
    public static LinkedList sumUp(LinkedList firstList, LinkedList secondList) {
        if (firstList.count() != secondList.count()) {
            return new LinkedList();
        }
        LinkedList sumList = new LinkedList();
        Node node1 = firstList.head;
        Node node2 = secondList.head;
        while (node1 != null) {
            sumList.addInTail(new Node(node1.value+node2.value));
            node1 = node1.next;
            node2 = node2.next;
        }
        return sumList;
    }
}

/*
Рефлексия.

Никаких рекомендаций ещё не поступало, просто так совпало, что я делал задачи по заданию поздно вечером, а потом решил
дописать недостающие тесты и перечитать, написанное вчера. Нашёл грубую ошибку в планировании функции, пока анализировал
временную сложность функции, удаляющей все узлы с конкретным значением. Лучше больше кода и сложность O(n), нежели
повторное использование уже написанного кода, но сложность O(n^2). Подробности в файле LinkedList.java. См. описание
решений Задачи 2.
 */