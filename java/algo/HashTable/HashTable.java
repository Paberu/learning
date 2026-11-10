package HashTable;


import java.util.Random;

// Курс "Практика в программировании на АСД. Задание 8.
// Задача 1. Задача 2. В том, что касается "поизучайте" я профи. У меня половина прикладных вещей изучена так, что мне
// говорили: "Что ж, теория однозначно пять, практика... ну... допустим, пять с минусом, потому что совсем уж явных
// ошибок вроде бы нет...". Что могу сказать? Это безумно глобальная тема, становится понятным, как некоторые люди
// построили карьеру лишь на том, что доводили до совершенства семейство SHA-* и внедряли их повсеместно. Я лишь верхушку
// поскрёб, но уже проникся уважением.

public class HashTable {
    public int size;
    public int step;
    public String [] slots;
    public int salt;

    public HashTable(int sz, int stp) {
        size = sz;
        step = stp;
        slots = new String[size];
        for(int i = 0; i < size; i++)
            slots[i] = null;
        salt = 1 + new Random().nextInt(Integer.MAX_VALUE - 1);
    }

    public int hashFun(String value) {
        // Соль участвует в каждом символе. Прибавлять её к сумме один раз бесполезно:
        // ключи с одинаковой суммой кодов всё равно попадали бы в один слот.
        int hash = salt;
        for (int i = 0; i < value.length(); i++) {
            hash = 31 * hash + value.charAt(i);
        }
        return hash & 0x7fffffff;
    }

    public int seekSlot(String value) {
        int index = hashFun(value) % size;
        for (int i = 0; i < size; i++) {
            if (slots[index] == null)
                return index;
            index = (index + step) % size;
        }
        return -1;
    }

    public int put(String value) {
        int index = seekSlot(value);
        if (index > -1) {
            slots[index] = value;
            return index;
        }
        return -1;
    }

    public int find(String value) {
        int index = hashFun(value) % size;
        for (int i = 0; i < size; i++) {
            if (slots[index] == null)
                return -1;
            if (slots[index].equals(value)) {
                return index;
            }
            index = (index + step) % size;
        }
        return -1;
    }
}