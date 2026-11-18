package PowerSet;

import HashTable.HashTable;

public class PowerSet {
    // Курс "Практика в программировании на АСД. Задание 10.
    // Задача 1. Создайте реализующий множество класс PowerSet... поэтому для внутреннего хранения множества можно взять
    // даже стандартный список. Попробуем.

    private int length;
    private HashTable hashTable;

    public PowerSet() {
        length = 0;
        hashTable = new HashTable(40031, 13);
        // ваша реализация хранилища
    }

    public int size() {
        // количество элементов в множестве
        return length;
    }

    public void put(String value) {
        // всегда срабатывает
        if (hashTable.find(value) != -1)
            return;
        int index = hashTable.put(value);
        if (index != -1)
            length++;
    }

    public boolean get(String value) {
        // возвращает true если value имеется в множестве,
        // иначе false
        int index = hashTable.find(value);
        return index != -1;
    }

    public boolean remove(String value) {
        // возвращает true если value удалено
        // иначе false
        int index = hashTable.remove(value);
        if (index == -1)
            return false;
        length--;
        return true;
    }

    public PowerSet intersection(PowerSet set2) {
        // пересечение текущего множества и set2
        PowerSet intersection = new PowerSet();
        for (String key : hashTable.values()) {
            if (set2.get(key))
                intersection.put(key);
        }
        return intersection;
    }

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

    public PowerSet difference(PowerSet set2) {
        // разница текущего множества и set2
        PowerSet difference = new PowerSet();
        for (String key : hashTable.values()) {
            if (!set2.get(key))
                difference.put(key);
        }
        return difference;
    }

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
