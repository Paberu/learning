package NativeDictionary;

import java.lang.reflect.Array;
import java.util.Random;

class NativeDictionary<T> {
    public int size;
    public String [] slots;
    public T [] values;
    private int salt;
    private int step;
    private Class cls;

    public NativeDictionary(int sz, Class clazz) {
        size = sz;
        slots = new String[size];
        cls = clazz;
        values = (T[]) Array.newInstance(clazz, this.size);
        salt = 1 + new Random().nextInt(Integer.MAX_VALUE - 1);
        step = size < 4 ? 1 : (size / 2) - 1;
    }

    public int hashFun(String key)  {
        int hash = salt;
        for (int i = 0; i < key.length(); i++) {
            hash = 17 * hash + key.charAt(i);
        }
        return hash & 0x7fffffff;
    }

    public boolean isKey(String key) {
        int index = hashFun(key) % size;
        for (int i = 0; i < size; i++) {
            if (slots[index] == null)   // если будет remove(), незамедлительно убрать
                return false;
            if (slots[index].equals(key)) {
                return true;
            }
            index = (index + step) % size;
        }
        return false;
    }

    public void put(String key, T value) {
        // гарантированно записываем
        // значение value по ключу key
        // если гарантированно, значит словарь должен уметь расширяться
        int index = seekSlot(key);
        if (index == -1) {
            int newSize = size * 2;
            String[] newSlots = new String[newSize];
            T [] newValues = (T[]) Array.newInstance(cls, newSize);
            for (int i = 0; i < size; i++) {
                int newIndex = seekSlotInNewSlots(slots[i], newSize, newSlots);
                if (newIndex == -1)
                    throw new IllegalStateException("Программа оказалась в невозможном состоянии");
                newSlots[newIndex] = slots[i];
                newValues[newIndex] = values[i];
            }
            this.size =  newSize;
            this.slots = newSlots;
            this.values = newValues;
            index = seekSlot(key);    // надо заново пересчитать, таблица изменилась
        }
        slots[index] =  key;
        values[index] = value;
    }

    private int seekSlot(String key) {
        int index = hashFun(key) % size;
        for (int i = 0; i < size; i++) {
            if (slots[index] == null || slots[index].equals(key))   // добавляем новый ключ или перезаписываем значение у старого
                return index;                                       // а ведь забыл
            index = (index + step) % size;
        }
        return -1;
    }

    private int seekSlotInNewSlots(String key, int newSize, String[] newSlots) {
        int newIndex = hashFun(key) % newSize;
        if (newSlots[newIndex] == null)
            return newIndex;
        for (int i = 0; i < newSize; i++) {
            newIndex = (newIndex + step) % newSize;
            if (newSlots[newIndex] == null)
                return newIndex;
        }
        return -1;  // нештатная ситуация, здесь невозможно оказаться
    }

    public T get(String key) {
        // возвращает value для key,
        // или null если ключ не найден
        int index = hashFun(key) % size;
        for (int i = 0; i < size; i++) {
            if (slots[index] == null) {   // если будет remove(), незамедлительно убрать
                return null;
            }
            if (slots[index].equals(key)) {
                return values[index];
            }
            index = (index + step) % size;
        }
        return null;
    }
}