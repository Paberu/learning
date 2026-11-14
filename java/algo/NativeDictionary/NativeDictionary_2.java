package NativeDictionary;

import DynamicArray.DynArray;
import OrderedList.OrderedList_2;

import java.lang.reflect.Array;
import java.util.Random;

public class NativeDictionary_2 {
}

class SortedDictionary<T extends Comparable> {
    // Задача 5. Реализуйте класс NativeDictionary, как описано выше.
    // Исполнено. Пришлось добавить private полей и методов, но оно того стоило.
    public int size;
    public OrderedList_2<T> slots;
    public DynArray<T> values;
    private int salt;
    private int step;
    private Class cls;

    public SortedDictionary(int sz, Class clazz) {
        size = sz;
        slots = new OrderedList_2<T>(clazz, true);
        cls = clazz;
        // values = (T[]) Array.newInstance(clazz, this.size);
        values = new DynArray<T>(clazz);
        salt = 1 + new Random().nextInt(Integer.MAX_VALUE - 1);
        step = size < 4 ? 1 : (size / 2) - 1;
    }

    public boolean isKey(T key) {
        return slots.find(key) != -1;
    }

    public T get(T key) {
        int index = slots.find(key);
        if (index == -1)
            return null;
        return values.getItem(index);
    }

    public void put(T key, T value) {
        int index = slots.find(key);
        if (index != -1) {
            values.set(index, value);
            return;
        }
        slots.add(key);
        index = slots.find(key);
        values.insert(value, index);
    }

}


// Рефлексия. **Рекомендации по решению задач задания 5.**