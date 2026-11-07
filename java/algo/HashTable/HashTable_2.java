package HashTable;

public class HashTable_2 {
    public void ddos(HashTable hashTable) {
        // Исходная hashFun складывала коды символов. Строка из n копий символа с кодом size
        // имеет сумму n * size, то есть все такие ключи шли в один и тот же слот.
        char symbol = (char) hashTable.size;
        StringBuilder key = new StringBuilder();
        for (int i = 0; i < hashTable.size; i++) {
            key.append(symbol);
            hashTable.put(key.toString());
        }
    }
}

class DynamicHashTable {
    public int size;
    public int step;
    public String[] slots;

    public DynamicHashTable(int size, int step) {
        this.size = size;
        this.step = step;
        this.slots = new String[size];
        for(int i = 0; i < size; i++)
            this.slots[i] = null;
    }

    public int hashFun(String value) {
        int hash = 0;
        for (int i = 0; i < value.length(); i++) {
            hash += value.charAt(i);
        }
        return hash;
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
        if(index == -1) {
            int newSize = size * 2;
            String[] newSlots = new String[newSize];
            for (int i = 0; i < size; i++) {
                int newIndex = seekSlotInNewSlots(slots[i], newSize, newSlots);
                if (newIndex == -1)
                    throw new IllegalStateException("Программа оказалась в невозможном состоянии");
                newSlots[newIndex] = slots[i];
            }
            this.size =  newSize;
            this.slots = newSlots;
        }
        index = seekSlot(value);    // надо заново пересчитать, таблица изменилась
        slots[index] = value;
        return index;
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

    private int seekSlotInNewSlots(String value, int newSize, String[] newSlots) {
        int newIndex = hashFun(value) % newSize;
        if (newSlots[newIndex] == null)
            return newIndex;
        for (int i = 0; i < newSize; i++) {
            newIndex = (newIndex + step) % newSize;
            if (newSlots[newIndex] == null)
                return newIndex;
        }
        return -1;  // нештатная ситуация, здесь невозможно оказаться
    }
}

class MultiHashTable {
    public int size;
    public int step;
    public int k;
    public String [] slots;

    public static final int[] SIMPLE_WEIGHTS = {17, 19, 23, 29, 31};

    public MultiHashTable(int size, int step, int k) {
        this.size = size;
        this.step = step;
        this.k = k;
        this.slots = new String[size];
        for(int i = 0; i < size; i++)
            this.slots[i] = null;
    }

    public int hashFunK(String value, int kI) {
        int hash = 0;
        int weight = SIMPLE_WEIGHTS[kI%SIMPLE_WEIGHTS.length];
        for (int i = 0; i < value.length(); i++) {
            hash += value.charAt(i) * (kI + 1) + weight;  // да, отбитая функция, зато сам делал )))
        }
        return (hash + weight + kI);
    }

    public int seekSlot(String value) {
        int[] hash_indexes = new int[k];
        for (int i = 0; i < k; i++) {
            hash_indexes[i] = hashFunK(value, i) % size;
        }
        for (int i = 0; i < k; i++) {
            if (slots[hash_indexes[i]] == null) {
                return hash_indexes[i]; // если нашёлся индекс по одной из k i-ых функций, то и красота, иначе пробирование
            }
        }
        for (int j = 0; j < size; j++) {
            for (int i = 0; i < k; i++) {
                hash_indexes[i] = (hash_indexes[i] + step) % size;
                if (slots[hash_indexes[i]] == null) {
                    return hash_indexes[i]; // на каждом шаге проверяем, вдруг один из слотов свободен
                }
            }
        }
        return -1; // таблица полна под завязку
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
        int[] hash_indexes = new int[k];
        for (int i = 0; i < k; i++) {
            hash_indexes[i] = hashFunK(value, i) % size;
        }
        for (int i = 0; i < k; i++) {
            if (slots[hash_indexes[i]] != null && slots[hash_indexes[i]].equals(value)) {
                return hash_indexes[i]; // эквивалентно seekSlot()
            }
        }
        for (int j = 0; j < size; j++) {
            for (int i = 0; i < k; i++) {
                hash_indexes[i] = (hash_indexes[i] + step) % size;
                if (slots[hash_indexes[i]] != null && slots[hash_indexes[i]].equals(value)) {
                    return hash_indexes[i]; // на каждом шаге проверяем, вдруг значение там
                }
            }
        }
        return -1;  // обошли всю таблицу, нет его
    }
}

