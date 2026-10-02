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

    public void insert(T itm, int[] indexes) {
        if (indexes.length != this.capacities.length) {
            throw new IllegalArgumentException("Количество индексов должно совпадать с размерностью массива.");
        }

        // 1. Проверяем, не выходят ли запрашиваемые индексы за текущую емкость (capacities)
        boolean needExpand = false;
        int[] newCapacities = this.capacities.clone();

        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < 0) {
                throw new IndexOutOfBoundsException("Индекс не может быть отрицательным.");
            }

            // Если индекс больше или равен текущей емкости — ось нужно расширять!
            if (indexes[i] >= this.capacities[i]) {
                needExpand = true;
                // Умножаем емкость оси на 2, пока она не станет строго больше запрашиваемого индекса
                while (newCapacities[i] <= indexes[i]) {
                    newCapacities[i] *= 2;
                }
            }
        }

        // 2. Если обнаружили нехватку места по какой-то оси, вызываем наш makeArray
        if (needExpand) {
            makeArray(newCapacities);
        }

        // 3. Обновляем counts для каждого измерения
        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] >= this.counts[i]) {
                this.counts[i] = indexes[i] + 1;
            }
        }

        // 4. Записываем элемент по вычисленному линейному индексу
        int linearIndex = getLinearIndex(indexes, this.steps);
        this.array[linearIndex] = itm;
    }

    public void remove(int[] indexes) {
        if (indexes.length != this.capacities.length) {
            throw new IllegalArgumentException("Количество индексов должно совпадать с размерностью массива.");
        }

        // 1. Валидация границ
        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < 0 || indexes[i] >= this.capacities[i]) {
                throw new IndexOutOfBoundsException("Индекс за пределами массива.");
            }
        }

        // 2. Зануляем удаляемый элемент
        int linearIndex = getLinearIndex(indexes, this.steps);
        this.array[linearIndex] = null;

        // 3. Пересчитываем counts[i] для осей.
        // Нам нужно узнать новый максимальный занятый индекс по каждой оси, так как мы могли удалить "крайний" элемент.
        recalculateCounts();

        // 4. Проверяем условия сжатия массива
        boolean needShrink = false;
        int[] newCapacities = this.capacities.clone();

        for (int i = 0; i < this.capacities.length; i++) {
            // Условие: заполненность (counts) строго меньше половины емкости (capacities / 2)
            // И при этом текущая емкость строго больше минимальной
            if (this.counts[i] < (double) this.capacities[i] / 2 && this.capacities[i] > MINIMUM_CAPACITY) {
                int shrunkCapacity = (int) (this.capacities[i] / 1.5);

                // Новая емкость не должна упасть ниже MINIMUM_CAPACITY
                newCapacities[i] = Math.max(shrunkCapacity, MINIMUM_CAPACITY);

                // Также новая емкость не должна урезать уже существующие элементы (counts)
                if (newCapacities[i] < this.counts[i]) {
                    newCapacities[i] = this.counts[i];
                }

                if (newCapacities[i] != this.capacities[i]) {
                    needShrink = true;
                }
            }
        }

        // 5. Если какое-то измерение можно сузить, вызываем makeArray
        if (needShrink) {
            makeArray(newCapacities);
        }
    }

    // Вспомогательный метод для обновления counts на основе оставшихся в массиве элементов
    private void recalculateCounts() {
        // Сбрасываем счетчики
        for (int i = 0; i < this.counts.length; i++) {
            this.counts[i] = 0;
        }

        // Рекурсивно или плоским перебором находим максимальные индексы ненулевых элементов
        for (int i = 0; i < this.array.length; i++) {
            if (this.array[i] != null) {
                // Переводим плоский индекс i обратно в N-мерные координаты
                int tempIndex = i;
                for (int d = 0; d < this.capacities.length; d++) {
                    int coord = tempIndex / this.steps[d];
                    if (coord + 1 > this.counts[d]) {
                        this.counts[d] = coord + 1;
                    }
                    tempIndex %= this.steps[d];
                }
            }
        }
    }


}
