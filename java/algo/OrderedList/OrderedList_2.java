package OrderedList;


import java.lang.reflect.Array;

public class OrderedList_2<T extends Comparable> {
    // Задача 12. Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна
    // работать за O(log N). Внутреннюю реализацию списка для этого можно сменить.
    private T[] array;
    private int size;
    private int capacity;
    private final boolean ascending;
    private final Class<T> clazz;

    private final static int MIN_CAPACITY = 16;

    public OrderedList_2(Class<T> clazz, boolean asc) {
        this.clazz = clazz;
        this.ascending = asc;
        this.capacity = MIN_CAPACITY;
        this.size = 0;
        this.array = (T[]) Array.newInstance(clazz, this.capacity);
    }

    public int size() {
        return this.size;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public int compare(T v1, T v2) {
        if (v1 == null || v2 == null) {
            throw new IllegalArgumentException("Ни один из аргументов не может быть null");
        }
        return Integer.signum(v1.compareTo(v2));
    }

    public void add(T value) {
        if (size == capacity)
            resize(2 * capacity);

        boolean check = (compare(array[size-1], value) <= 0 && ascending) || (compare(array[size-1], value) >= 0 && !ascending);
        if (check) {        // вставка в хвост
            array[size] = value;
            return;
        }

        check = (compare(array[0], value) >= 0 && ascending) || (compare(array[0], value) <= 0 && !ascending);
        if (check) {        // вставка в голову
            System.arraycopy(array, 0, array, 1, size);
            array[0] = value;
            return;
        }

        // ни в хвост, ни в гриву
        int index = findInsertIndex(value);
        System.arraycopy(array, index, array, index+1, size-index);
        array[index] = value;
        size++;
    }

    private void resize(int newCapacity) {
        if (newCapacity < MIN_CAPACITY)
            newCapacity = MIN_CAPACITY;
        if (newCapacity == this.capacity)
            return;

        T[] newArray =  (T[]) Array.newInstance(clazz, newCapacity);
        System.arraycopy(this.array, 0, newArray, 0, this.size);

        this.array = newArray;
        this.capacity = newCapacity;
    }

    private int findInsertIndex(T value) {
        int index = size / 2;
        return index;
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


// Рефлексия. **Рекомендации по решению задач задания 5.**

/**
3. **Вращение очереди по кругу на N элементов**.
В цикле до N выталкиваем элемент с одного конца, и вталкиваем его с другого.
*/
/*
Особенно приятно то, что пришёл к этой мысли ещё до того, как взял бумажку, ручку и начал прикидывать, что я могу сделать
при такой постановке задачи. Единственный момент, достойный внимания - это отрицательное смещение. Когда в цикле for
оказывается проходка от 0 до -4 с шагом i++, понимаешь, что надо привести смещение к положительному значению. В остальном,
всё прошло как по маслу.
*/

/**
4. **Очередь с помощью двух стеков**.
Идея, что кладём всегда в один стек, больше ничего не делая, за O(1),
а забираем всегда из другого, причём перегоняем в него всё из первого стека, только если данный стек пуст (асимптотика
получается близкой к o(1)) .
*/
/*
Лучшей иллюстрацией моего решения будет комментарий, описывающий работу этой функции, который я оставил перед коммитом:
Мы дважды перекладываем из одного стека в другой, целиком. Сегодня на работе я рисовал, как плавают значения из стека в
стек и понял, что достаточно перекладывать всё из первой очереди во вторую, лишь когда вторая полностью опустеет из-за
dequeue(). В таком случае все операции будут O(1). Но я оставляю вчерашнее решение, что называется, "в лоб", благодаря
которому "вся дурость видна". Этот комментарий и нижеследующее решение будут напоминанием: не все хорошие решения приходят
сразу, иногда следует сделать то, что работает, а на следующий день, с утра, можно переделать, с O(n) на O(1). Главное,
не сломать интерфейсы, меняя реализацию.
*/

/**
5. **Обращение всех элементов в очереди в обратном порядке**.
Используем стек: поочередно извлекаем элементы из очереди и добавляем их в стек,
а затем извлекаем элементы из стека и снова добавляем их в очередь.
*/
/*
Почему-то не сразу понял, что следует использовать свои же наработки из прошлых заданий. Думал про перекладывание из
очереди в очередь и обратно, ещё какие-то идейки, а потом нарисовал на бумаге, как следует реализовать перекладку, и
подумал: "У меня ж стек буквально на прошлом задании реализован!". И "тут мне как попёрло".
*/

/*
6. **Циклическая буферную очередь на базе статического массива фиксированного размера.**.
Указатель head указывает на начало очереди (первый элемент).
Указатель tail указывает на позицию, куда будет добавлен следующий элемент.
Изначально оба указателя установлены в 0.
*** много текста ***
*/

/*
Я внаглую спёр переменные и их смысл из задания про динамический массив: capacity и size. Если их значения совпадают,
значит очередь полна. Если разошлись, значит можно докинуть ещё. Выполнял под вечер и жёстко тупил: постоянно терял 1
при кольцевом переводе begin и end через [% capacity] и не могу понять, почему перезаписываются значения, когда в очереди
ещё есть пустые места. Debug - наше всё.
*/