package DynamicArray;

import java.lang.reflect.Array;

public class DynArray_2<T> {
    // Курс "Практика в программировании на АСД. Задание 3.
    // Задание 6. Динамический массив на основе банковского метода амортизационного анализа.
    // Структура данных уже реализована на основе указанного метода, т.к. это техника анализа, а не реализации.
    // Рассмотрим функцию append():
    // Реальная стоимость: O(1) в среднем, O(n) при расширении. Но нас-то интересует амортизированная стоимость:
    // при прохождении подобного курса на Python каждой операции присваивали 3 токена.
    // 1 токен тратится при добавлении элемента в конец списка, а 2 попадают на "банковский счёт".
    // Т.е., если нарушить общепринятую нотацию, добавление элемента - О(3), а не О(1).
    // При расширении встроенного массива вдвое происходит копирование элементов, эти затраты учитываются со "счёта", т.е.
    // если в массиве уже n элементов, то на "счёте" находится 2*n токенов, из которых n вычитается при учёте операции
    // копирования. Т.к. операция копирования стоит O(1), но на балансе находится уже не 2*n, а n токенов.
    // При дальнейшем расширении динамического массива баланс только продолжает нарастать.

    // Задание 7. Реализуйте многомерный динамический массив: произвольное количество измерений, при этом каждое
    // измерение может внутри масштабироваться по потребности.
    private T [] array;
    private int[] counts;
    private int[] capacities;
    private int dimensions;
    Class clazz;

    public DynArray_2(Class clz, int dimensions, int[] capacities) {
        if (dimensions != capacities.length) {
            throw new IllegalArgumentException("Число размерностей измерений не соответствует указанному количеству измерений");
        }
        this.clazz = clz; // нужен для безопасного приведения типов
        // new DynArray<Integer>(Integer.class);
        this.dimensions = dimensions;
        this.counts = new int[]{};
        this.capacities = capacities.clone();
        makeArray(capacities);
    }

    public void makeArray(int[] newCapacities) {
        for (int i = 0; i < newCapacities.length; i++) {
            if (newCapacities[i] <= 16)
                newCapacities[i] = 16;
        }

        boolean needs_to_remake = false;
        for (int i = 0; i < newCapacities.length; i++) {
            if (newCapacities[i] != this.capacities[i])
                needs_to_remake = true;
                break;
        }
        if (!needs_to_remake) return;

        T[] temp_array = (T[]) Array.newInstance(this.clazz, this.dimensions, newCapacities);

        int totalCount = 0;
        for (int count : this.counts) {
            totalCount += count;
        }
        if (this.array != null) {
            for (int i = 0; i < totalCount; i++) {
                temp_array[i] = this.array[i];
            }
        }
        this.array = temp_array;
        this.capacities = newCapacities;
    }

}
