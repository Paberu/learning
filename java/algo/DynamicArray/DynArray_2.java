package DynamicArray;

import java.lang.reflect.Array;
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



public class DynArray_2<T> {
    // Задание 7. Реализуйте многомерный динамический массив: произвольное количество измерений, при этом каждое
    // измерение может внутри масштабироваться по потребности.
    public static final int MINIMUM_CAPACITY = 4;   // для удобства тестирования, мне же принцип понять надо

    private T[] array;
    private int[] capacities;
    private int[] steps;
    private int[] counts;
    Class clazz;

    public DynArray_2(Class<T> clz, int dimensions, int... capacities) {
        if (dimensions != capacities.length) {
            throw new IllegalArgumentException("Размерность должна совпадать с количеством измерений.");
        }
        this.clazz = clz;
        this.capacities = capacities.clone();
        this.steps = calculateSteps(capacities);
        this.counts = new int[capacities.length];
        this.array = (T[]) Array.newInstance(this.clazz, getTotalSize());
    }

    public int getTotalSize() {
        return getTotalSize(this.capacities);
    }

    private int getTotalSize(int[] newCapacities) {
        int totalSize = 1;
        for (int capacity : newCapacities) {
            totalSize *= capacity;
        }
        return totalSize;
    }

    private int getLinearIndex(int[] axises, int[] steps) {
        int linearIndex = 0;
        for (int i = 0; i < axises.length; i++){
            linearIndex += axises[i] * steps[i];
        }
        return linearIndex;
    }

    public void makeArray(int[] newCapacities) {
        int[] newCaps = new int[newCapacities.length];
        for (int i = 0; i < newCapacities.length; i++) {
            newCaps[i] = Math.max(newCapacities[i], MINIMUM_CAPACITY);
        }

        if (!needsToRemake(newCaps)) return;

        int[] newSteps = calculateSteps(newCaps);
        T[] temp_array = (T[]) Array.newInstance(this.clazz, getTotalSize(newCaps));

        int[] currentCoordinates = new int[this.capacities.length];
        copyElementsRecursively(temp_array, newSteps, currentCoordinates, 0);
        this.capacities = newCaps;
        this.steps = newSteps;
        this.array = temp_array;
    }

    private void copyElementsRecursively(T[] temp_array, int[] newSteps, int[] currentCoordinates, int currentDimension) {
        if (currentDimension == this.capacities.length) {
            int oldLink = getLinearIndex(currentCoordinates, this.steps);
            int newLink = getLinearIndex(currentCoordinates, newSteps);
            temp_array[newLink] = this.array[oldLink];
            return;
        }

        for (int i = 0; i < this.counts[currentDimension]; i++) {
            currentCoordinates[currentDimension] = i;
            copyElementsRecursively(temp_array, newSteps, currentCoordinates, currentDimension + 1);
        }
    }

    public boolean needsToRemake(int[] capacitiesToCheck) {
        for (int i = 0; i < capacitiesToCheck.length; i++) {
            if (capacitiesToCheck[i] != this.capacities[i]) {
                return true;
            }
        }
        return false;
    }

    private static int[] calculateSteps(int... capacities) {
        int totalCapacities = capacities.length;
        int[] steps = new int[totalCapacities]; // при движении по осям x,y,z, например, в кубе значений 10*10*10, смещение по оси x в одномерном массиве равно 1, по оси y - 10, по оси z - 100.
        steps[totalCapacities -1] = 1;           // начинаем с оси x (у которой 1).
        for (int i = totalCapacities - 2; i >=0; i--) {
            steps[i] = steps[i+1] * capacities[i+1];    //смещение по следующей оси равно смещению по текущей оси, помноженному на размерность этой оси.
        }
        return steps;
    }

    public T getItem(int... indexes) {
        if (indexes.length != this.capacities.length) {
            throw new IllegalArgumentException("Indexes count must be equal to array dimensions.");
        }
        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < 0 || indexes[i] >= this.counts[i]) {
                throw new IndexOutOfBoundsException("Index is out of bounds");
            }
        }
        int linearIndex = getLinearIndex(indexes, this.steps);
        return this.array[linearIndex];
    }

    public void append(T itm) {

    }

    public void insert(T itm, int[] indexes){

    }

    public void remove(int[] indexes) {

    }

}
