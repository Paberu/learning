package OrderedList;


public class OrderedList_2 {
    // Задача 2. Метод сравнения двух значений.
    // Сложность решения по времени: O(n). Приходится пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public static void removeDuplicate(OrderedList ol) {
        Node startNode = ol.head;
        while (startNode != ol.tail) {
            Node tempNode = startNode.next;
            if (ol.compare(startNode.value, tempNode.value) == 0) {
                do {
                    startNode.next = tempNode.next;
                    tempNode.next.prev = startNode;
                    tempNode = tempNode.next;       // где должна быть проверка на хвост?
                } while (ol.compare(tempNode.value, tempNode.next.value) == 0);
                tempNode.next = null;
                tempNode.prev = null;
            }
            startNode = startNode.next;
        }

    }
}
