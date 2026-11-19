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
        if (listOfSets == null || listOfSets.isEmpty()) {
            return new PowerSet();
        }
        PowerSet result = listOfSets.get(0);
        for (int i = 1; i < listOfSets.size(); i++) {
            result = result.intersection(listOfSets.get(i));
        }
        return result;
    }

}

class Bag {

    private int length;
    private HashTable hashTable;

    public Bag() {
        length = 0;
        hashTable = new HashTable(20000, 13);
    }

    public int size() {
        return length;
    }

    public ArrayList<String> values() {
        return hashTable.values();
    }

    public void put(String value) {
        int index = hashTable.put(value);
        if (index != -1)
            length++;
    }

    public boolean get(String value) {
        int index = hashTable.find(value);
        return index != -1;
    }

    public boolean remove(String value) {
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
