package OrderedList;


import DynamicArray.DynArray;

import java.util.HashMap;

public class OrderedList_2<T extends Comparable> {
    // Задача 12. Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна
    // работать за O(log N). Внутреннюю реализацию списка для этого можно сменить.
    private DynArray<T> array;
    private boolean ascending;

    public OrderedList_2(boolean asc) {
        ascending = asc;
        array = new DynArray<>(array.getClass());
    }



    // Задача 8. Добавьте метод удаления всех дубликатов из упорядоченного списка.
    // Сложность решения по времени: O(n). Приходится пробежать весь список.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public static <T extends Comparable> void removeDuplicate(OrderedList<T> ol) {
        Node<T> startNode = ol.head;
        while (startNode != null && startNode.next != null) {
            Node<T> tempNode = startNode.next;
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
    public static <T extends Comparable> OrderedList<T> concatenateLists(OrderedList<T> ol1, OrderedList<T> ol2) {
        if (ol1.getAsc() != ol2.getAsc()) throw new IllegalArgumentException("Списки должны быть упорядочены в одном и том же направлении!");
        OrderedList<T> resultList = new OrderedList<T>(ol1.getAsc());
        Node<T> current1 = ol1.head;
        Node<T> current2 = ol2.head;
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
    // Сложность решения по времени: O(n). Придётся пройти весь список.
    // Сложность решения по пространству: О(1). Сначала использовал hashmap, сложность была O(n), потом отвлёкся, перечитал
    // задание, заметил, что список-то упорядоченный по значениям, значит хватит двух переменных - значение и счётчик.
    public static <T extends Comparable> T getMostFrequent(OrderedList<T> ol) {
        if (ol.head == null) return null;
        T mostFrequentValue = ol.head.value;
        int greatestCount = 0;
        Node<T> currentNode = ol.head;
        while (currentNode != null) {
            T value = currentNode.value;
            int count = 0;
            while (currentNode != null && ol.compare(value, currentNode.value) == 0) {
                count++;
                currentNode = currentNode.next;
            }
            if (count > greatestCount) {
                greatestCount = count;
                mostFrequentValue = value;
            }
        }
        return mostFrequentValue;
    }
}


// Рефлексия.

/*
**Рекомендации по решению задач задания 5.**

3. **Вращение очереди по кругу на N элементов**.
В цикле до N выталкиваем элемент с одного конца, и вталкиваем его с другого.

4. **Очередь с помощью двух стеков**.
Идея, что кладём всегда в один стек, больше ничего не делая, за O(1),
а забираем всегда из другого, причём перегоняем в него всё из первого стека, только если данный стек пуст (асимптотика получается близкой к o(1)) .

5. **Обращение всех элементов в очереди в обратном порядке**.
Используем стек: поочередно извлекаем элементы из очереди и добавляем их в стек,
а затем извлекаем элементы из стека и снова добавляем их в очередь.

6. **Циклическая буферную очередь на базе статического массива фиксированного размера.**.
Указатель head указывает на начало очереди (первый элемент).
Указатель tail указывает на позицию, куда будет добавлен следующий элемент.
Изначально оба указателя установлены в 0.

Добавление элемента:
- Если очередь не заполнена, элемент добавляется в позицию tail.
- После добавления tail увеличивается на 1. Если tail достигает конца массива, он "перескакивает" на начало:
tail = (tail + 1) % размер_массива
- Если tail "догоняет" head, это означает, что очередь заполнена, и добавление нового элемента невозможно.

Удаление элемента:
- Если очередь не пуста, элемент извлекается из позиции head.
- После извлечения head увеличивается на 1. Если head достигает конца массива, он "перескакивает" на начало:
head = (head + 1) % размер_массива
- Если head и tail совпадают после удаления, это означает, что очередь пуста.

Очередь пуста, если head == tail.
Очередь заполнена, если (tail + 1) % размер_массива == head.
Для корректной работы всегда нужно оставлять одну пустую ячейку между head и tail, чтобы различать состояния "пусто" и "полно".

Если нужно отслеживать количество элементов в очереди, можно использовать отдельную переменную-счётчик.
*
* 
 */
