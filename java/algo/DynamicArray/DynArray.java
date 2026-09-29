package DynamicArray;

import java.lang.reflect.Array;

public class DynArray<T> {
    public T [] array;
    public int count;
    public int capacity;
    Class clazz;

    public DynArray(Class clz) {
        this.clazz = clz; // нужен для безопасного приведения типов
        // new DynArray<Integer>(Integer.class);
        this.count = 0;
        this.capacity = 0;
        makeArray(16);
    }

    // Курс "Практика в программировании на АСД. Задание 3.
    // Задача 1. Реализовать базовые методы: makeArray(), getItem(), append().

    // Сложность решения по времени: O(n). Всегда надо пробежать весь список при копировании значений в новый.
    // Сложность решения по пространству: О(n). Всегда создаётся новый список, старый сотрёт сборщик мусора.
    public void makeArray(int new_capacity) {
        // ваш код
        if (new_capacity <= 16)
            new_capacity = 16;
        if (new_capacity == this.capacity) return;

        T[] temp_array = (T[]) Array.newInstance(this.clazz, new_capacity);
        if (this.array != null) {
            for (int i = 0; i < this.count; i++) {
                temp_array[i] = this.array[i];
            }
        }
        this.array = temp_array;
        this.capacity = new_capacity;
    }

    // Сложность решения по времени: O(1). Просто берётся указанный элемент по смещению, указанному в аргументе.
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public T getItem(int index) {
        // ваш код
        if (index < 0 || index >= count) {
            throw new IndexOutOfBoundsException("Index is out of bounds");
        }
        return this.array[index];
    }

    // Сложность решения по времени: O(1). При расчёте по банковскому методу на серию "дешёвых" операций по добавлению в массив приходится одна "дорогая" по расширению массива. На балансе - О(1).
    // Сложность решения по пространству: О(1). Ничего нового не создаётся.
    public void append(T itm) {
        // ваш код
        if (this.count == this.capacity) {
            makeArray(2*this.capacity);
        }
        this.array[count] = itm;
        this.count++;
    }

    public void insert(T itm, int index) {
        // ваш код
        if (index < 0 || index > this.count) {          // если индекс больше, чем кол-во элементов, то какой же это insert?
            throw new IndexOutOfBoundsException("Index is out of bounds");
        }

        if (index == this.count) {                      // а если равен кол-во, то это просто добавление в конец
            append(itm);
            return;
        }

        if (this.count == this.capacity) {              // меняем ёмкость, если уже некуда вставлять
            makeArray(2 * capacity);
        }
        for (int i = this.count; i > index; i--) {      // сдвигаем на соседнюю ячейку вправо вплоть до index...
            this.array[i] = this.array[i-1];
        }
        this.array[index] = itm;                        // .. и вставляем элемент куда нужно
        this.count++;
    }

    public void remove(int index) {
        // ваш код
        if (index < 0 || index >= this.count) {
            throw new IndexOutOfBoundsException("Index is out of bounds");
        }

        for (int i = index; i < this.count - 1; i++) {
            this.array[i] = this.array[i+1];
        }
        this.array[this.count-1] = null;
        this.count--;

        if (this.count < this.capacity / 2) {
            makeArray((int)(this.capacity/1.5));
        }
    }

}