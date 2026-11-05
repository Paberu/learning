package HashTable;


public class HashTable
{
    public int size;
    public int step;
    public String [] slots;

    public HashTable(int sz, int stp) {
        size = sz;
        step = stp;
        slots = new String[size];
        for(int i = 0; i < size; i++)
            slots[i] = null;
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