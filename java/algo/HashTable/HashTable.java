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
        for(int i=0; i<size; i++) slots[i] = null;
    }

    public int hashFun(String value) {
        int hash = 0;
        for (int i = 0; i < value.length(); i++) {
            hash += value.charAt(i);
        }
        return hash;
    }

    public int seekSlot(String value) {
        int hash = hashFun(value);
        if (slots[hash] == null) {
            return hash;
        }

        return -1;
    }

    public int put(String value)
    {
        // записываем значение по хэш-функции

        // возвращается индекс слота или -1
        // если из-за коллизий элемент не удаётся разместить
        return -1;
    }

    public int find(String value)
    {
        // находит индекс слота со значением, или -1
        return -1;
    }
}