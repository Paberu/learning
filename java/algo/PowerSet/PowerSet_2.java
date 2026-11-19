package PowerSet;

import HashTable.HashTable;

import java.util.ArrayList;
import java.util.HashMap;

public class PowerSet_2 {

    public static PowerSet decartMultiply(PowerSet first, PowerSet second) {
        PowerSet result = new PowerSet();
        for (String key1 : first.values()) {
            for (String key2 : second.values()) {
                result.put(key1+","+key2);
            }
        }
        return result;
    }

    public static PowerSet multiIntersect(ArrayList<PowerSet> listOfSets) {
        PowerSet result = listOfSets.getFirst();
        for (PowerSet nextSet : listOfSets) {
            result = result.intersection(nextSet);
        }
        return result;
    }
}

class Bag {
    // Курс "Практика в программировании на АСД. Задание 10.
    // Задача 1. Создайте реализующий множество класс PowerSet... поэтому для внутреннего хранения множества можно взять
    // даже стандартный список. Попробуем.
    private int length;
    private HashTable hashTable;

    public Bag() {
        length = 0;
        hashTable = new HashTable(20000, 13);
        // ваша реализация хранилища
    }

    public int size() {
        // количество элементов в множестве
        return length;
    }

    public ArrayList<String> values() {
        return hashTable.values();
    }

    public void put(String value) {
        // всегда срабатывает
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

    public HashMap<String, Integer> getAll() {
        HashMap<String, Integer> values = new HashMap<>();
        for (String value : hashTable.values()) {
            values.merge(value, 1, Integer::sum);
        }
        return values;
    }
}
