package OrderedList;


public class OrderedList_2 {
    // Задача 8. Добавьте метод удаления всех дубликатов из упорядоченного списка.
    // Сложность решения по времени: O(n). Приходится пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public static void removeDuplicate(OrderedList ol) {
        Node startNode = ol.head;
        while (startNode != null && startNode.next != null) {
            Node tempNode = startNode.next;
            if (ol.compare(startNode.value, tempNode.value) == 0) {
                startNode.next = tempNode.next;
                if (tempNode.next != null) {
                    tempNode.next.prev = startNode;
                } else {
                    ol.tail = startNode;
                }
                tempNode.next = null;
                tempNode.prev = null;
            } else {
                startNode = startNode.next;
            }
        }
    }

    // Задача 9. Напишите алгоритм слияния двух упорядоченных списков в один, сохраняя порядок элементов.
    // Сложность решения по времени: O(n+m). Придётся линейно пройти оба списка.
    // Сложность решения по пространству: О(n+m). Создаётся новый список длиной в два предыдущих. Это лучшее, что я смог
    // придумать, потому что менять списки, переданные в качестве аргументов - дурной тон.
    public static OrderedList concatenateLists(OrderedList ol1, OrderedList ol2) {
        if (ol1.getAsc() != ol2.getAsc()) throw new IllegalArgumentException("Списки должны быть упорядочены в одном и том же направлении!");
        OrderedList resultList = new OrderedList(ol1.getAsc());
        Node current1 = ol1.head;
        Node current2 = ol2.head;
        while (current1 != null && current2 != null) {
            boolean firstSmaller = ol1.compare(current1.value, current2.value) <= 0;
            if ((firstSmaller && ol1.getAsc()) || (!firstSmaller && !ol1.getAsc())) {
                resultList.add(current1.value);
                current1 = current1.next;
            } else {
                resultList.add(current2.value);
                current2 = current2.next;
            }
        }
        while (current1 != null) {
            resultList.add(current1.value);
            current1 = current1.next;
        }
        while (current2 != null) {
            resultList.add(current2.value);
            current2 = current2.next;
        }
        return resultList;
    }

    // Задача 10. Напишите метод проверки наличия заданного упорядоченного под-списка (параметр метода) в текущем списке.
    // Сложность решения по времени: O(n+m). Придётся линейно пройти оба списка.
    // Сложность решения по пространству: О(1). Создаётся несколько новых переменных.
    public static boolean checkEntry(OrderedList mainList, OrderedList subList) {
        if (mainList.getAsc() != subList.getAsc()) return false;
        Node mainStart = mainList.head;
        Node subStart = subList.head;
        while (mainStart != null && subStart != null) {
            int compare = mainList.compare(mainStart.value, subStart.value);
            if (compare == 0) {
                mainStart = mainStart.next;
                subStart = subStart.next;
            } else if ((compare < 0 && mainList.getAsc()) || (compare > 0 && !mainList.getAsc())) {
                mainStart = mainStart.next;
            } else {
                return false;
            }
        }
        return subStart == null;
    }


    // Задача 11. Добавьте метод, который находит наиболее часто встречающееся значение в списке.
    // Сложность решения по времени: O(n+m). Придётся линейно пройти оба списка.
    // Сложность решения по пространству: О(n+m). Создаётся новый список длиной в два предыдущих. Это лучшее, что я смог
    // придумать, потому что менять списки, переданные в качестве аргументов - дурной тон.
}
