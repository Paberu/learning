package HashTable;

public class HashTable_2 {
    public void ddos(HashTable hashTable) {

    }

}

class DynamicHashTable {

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
            hash += value.charAt(i) * weight + kI;  // да, отбитая функция, зато сам делал )))
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

