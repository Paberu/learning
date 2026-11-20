package PowerSet;

import HashTable.HashTable;

import java.util.ArrayList;

public class PowerSet {
    // Курс "Практика в программировании на АСД. Задание 10.
    // Задача 1. Создайте реализующий множество класс PowerSet. Попробуем.

    private int length;
    private HashTable hashTable;

    public PowerSet() {
        length = 0;
        hashTable = new HashTable(20000, 13);
        // ваша реализация хранилища
    }

    // Сложность решения по времени - О(1).
    // Сложность решения по пространству - О(1).
    public int size() {
        // количество элементов в множестве
        return length;
    }

    // Сложность решения по времени - О(n). Пробегается внутренний массив хэш-таблицы.
    // Сложность решения по пространству - О(n). Создаётся список значений из этого массива.
    public ArrayList<String> values() {
        return hashTable.values();
    }

    // Сложность решения по времени - О(1). Расчёт индекса зависит от длины строки, а не от заполненности массива.
    // С другой стороны, при загруженности хэш-таблицы более, чем на 80% будет n-коллизий, и сложность по времени
    // устремится к О(n). Так что мне даже сложно нормально расчитать сложность наихудшего варианта.
    // Сложность решения по пространству - О(1). Добавляется в массив ещё одно значение.
    public void put(String value) {
        // всегда срабатывает
        if (hashTable.find(value) != -1)
            return;
        int index = hashTable.put(value);
        if (index != -1)
            length++;
    }

    // Сложность решения по времени - О(1). В базовом варианте, при загруженности менее половины, имхо, сложность
    // остаётся О(1). Но при росте количества коллизий сложность устремляется к О(n).
    // Сложность решения по пространству - О(1). Ничего нового не создаётся.
    public boolean get(String value) {
        // возвращает true если value имеется в множестве,
        // иначе false
        int index = hashTable.find(value);
        return index != -1;
    }

    // Сложность решения по времени - О(1). Аналогично двум предыдущим.
    // Сложность решения по пространству - О(1). Ничего нового не создаётся.
    public boolean remove(String value) {
        // возвращает true если value удалено
        // иначе false
        int index = hashTable.remove(value);
        if (index == -1)
            return false;
        length--;
        return true;
    }

    // Задача 2. Дополнительно реализуем следующие типичные для множества методы:
    // Сложность решения по времени - О(n+m). Пробегается содержимое обоих множеств.
    // Сложность решения по пространству - О(n). В случае полного совпадения двух множеств создаётся ещё один дубликат.
    public PowerSet intersection(PowerSet set2) {
        // пересечение текущего множества и set2
        PowerSet intersection = new PowerSet();
        for (String key : hashTable.values()) {
            if (set2.get(key))
                intersection.put(key);
        }
        return intersection;
    }

    // Сложность решения по времени - О(n+m). Пробегается содержимое обоих множеств.
    // Сложность решения по пространству - О(n+m). В случае отсутствия совпадений создаётся массив размером в оба множества.
    public PowerSet union(PowerSet set2) {
        // объединение текущего множества и set2
        PowerSet union = new PowerSet();
        for (String key : hashTable.values()) {
            union.put(key);
        }
        for (String key : set2.hashTable.values()) {
            union.put(key);
        }
        return union;
    }

    // Сложность решения по времени - О(n+m). Пробегается содержимое обоих множеств.
    // Сложность решения по пространству - О(n). В случае пустого второго множества создаётся копия первого.
    public PowerSet difference(PowerSet set2) {
        // разница текущего множества и set2
        PowerSet difference = new PowerSet();
        for (String key : hashTable.values()) {
            if (!set2.get(key))
                difference.put(key);
        }
        return difference;
    }

    // Сложность решения по времени - О(n). Пробегается содержимое второго множества.
    // Сложность решения по пространству - О(1). Возвращает булеву переменную.
    public boolean isSubset(PowerSet set2) {
        // возвращает true, если set2 есть
        // подмножество текущего множества,
        // иначе false
        for (String key : set2.hashTable.values()) {
            if (!get(key))
                return false;
        }
        return true;
    }

    // Сложность решения по времени - О(n+m). Пробегается содержимое обоих множеств.
    // Сложность решения по пространству - О(1). Возвращает булеву переменную.
    public boolean equals(PowerSet set2) {
        // возвращает true,
        // если set2 равно текущему множеству,
        // иначе false
        if (length != set2.length)
            return false;
        for (String key : hashTable.values()) {
            if (!set2.get(key))
                return false;
        }
        return true;
    }
}
