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
    private int totalCount = 0;
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

    public void makeArray(int[] newCapacities) {
        int[] newCaps = new int[newCapacities.length];
        for (int i = 0; i < newCapacities.length; i++) {
            newCaps[i] = Math.max(newCapacities[i], MINIMUM_CAPACITY);
        }

        if (!needsToRemake(newCaps)) return;

        int[] newSteps = calculateSteps(newCaps);
        T[] temp_array = (T[]) Array.newInstance(this.clazz, getTotalSize(newCaps));

        if (this.totalCount > 0) {
            System.arraycopy(this.array, 0, temp_array, 0, this.totalCount);
        }
        this.capacities = newCaps;
        this.steps = newSteps;
        this.array = temp_array;

        recalculateCounts();
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
        int freeCellIndex = this.totalCount;
        if (freeCellIndex >= this.array.length) {
            int dimensionForExpand = getDimensionToExpand();
            int[] newCapacities = this.capacities.clone();
            newCapacities[dimensionForExpand] *= 2;

            makeArray(newCapacities);
        }
        this.array[freeCellIndex] = itm;
        this.totalCount++;

        int tempIndex = freeCellIndex;
        for (int i = 0; i < this.capacities.length; i++) {
            int coordinate = tempIndex / this.steps[i];
            if (coordinate >= this.counts[i]) {
                this.counts[i] = coordinate + 1;
            }
            tempIndex %= this.steps[i];
        }

    }

    public void insert(T itm, int... indexes) {
        if (indexes.length != this.capacities.length) {
            throw new IllegalArgumentException("Количество индексов должно совпадать с размерностью массива.");
        }

        // 1. Считаем целевой линейный индекс для вставки
        int targetLinearIndex = getLinearIndex(indexes, this.steps);

        // Валидация: в плотную структуру нельзя вставить элемент "в воздух" дальше текущего хвоста
        if (targetLinearIndex < 0 || targetLinearIndex > this.totalCount) {
            throw new IndexOutOfBoundsException("Вставка возможна только в существующий диапазон или в конец данных.");
        }

        // 2. Проверяем переполнение физической памяти
        if (this.totalCount >= this.array.length) {
            int dimToExpand = getDimensionToExpand(); // Ищем ось с наименьшей емкостью
            int[] newCapacities = this.capacities.clone();
            newCapacities[dimToExpand] *= 2;         // Удваиваем её

            makeArray(newCapacities);                // Перестраиваем структуру и обновляем steps

            // После изменения шагов (steps) старые N-мерные координаты будут указывать на другое плоское место!
            // Пересчитываем целевой плоский индекс в новых реалиях
            targetLinearIndex = getLinearIndex(indexes, this.steps);
        }

        // 3. Сдвигаем элементы вправо, освобождая ячейку для нового элемента
        if (this.totalCount - targetLinearIndex > 0) {
            System.arraycopy(this.array, targetLinearIndex, this.array, targetLinearIndex + 1, this.totalCount - targetLinearIndex);
        }

        // 4. Записываем элемент и инкрементируем общий счетчик
        this.array[targetLinearIndex] = itm;
        this.totalCount++;

        // 5. Пересчитываем counts для актуализации N-мерных границ
        recalculateCounts();
    }

    public void remove(int... indexes) {
        if (indexes.length != this.capacities.length) {
            throw new IllegalArgumentException("Количество индексов должно совпадать с размерностью массива.");
        }

        // Валидация границ через getItem (или по вашему условию)
        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < 0 || indexes[i] >= this.counts[i]) {
                throw new IndexOutOfBoundsException("Индекс за пределами заполненного массива.");
            }
        }

        // 1. Получаем плоский индекс удаляемого элемента
        int targetLinearIndex = getLinearIndex(indexes, this.steps);

        // 2. Сдвигаем все последующие элементы влево, уплотняя данные ("по циклу")
        int elementsToShift = this.totalCount - targetLinearIndex - 1;
        if (elementsToShift > 0) {
            System.arraycopy(this.array, targetLinearIndex + 1, this.array, targetLinearIndex, elementsToShift);
        }

        // Зануляем освободившийся хвост и декрементируем счетчик элементов
        this.array[this.totalCount - 1] = null;
        this.totalCount--;

        // 3. Актуализируем counts под новую заполненность
        recalculateCounts();

        // 4. Логика сжатия: проверяем заполненность по осям
        boolean needShrink = false;
        int[] newCapacities = this.capacities.clone();

        for (int i = 0; i < this.capacities.length; i++) {
            // Условие: заполненность (counts) строго меньше половины емкости (capacities / 2)
            // И текущая емкость позволяет уменьшение (строго больше MINIMUM_CAPACITY)
            if (this.counts[i] < (double) this.capacities[i] / 2 && this.capacities[i] > MINIMUM_CAPACITY) {
                // Находим ось, которую стратегически правильнее всего сжать (самую раздутую)
                int dimToShrink = getDimensionToShrink();

                int shrunkCapacity = (int) (newCapacities[dimToShrink] / 1.5);
                newCapacities[dimToShrink] = Math.max(shrunkCapacity, MINIMUM_CAPACITY);

                // Защита: новая емкость не должна отсечь уже существующие элементы по этой оси
                if (newCapacities[dimToShrink] < this.counts[dimToShrink]) {
                    newCapacities[dimToShrink] = this.counts[dimToShrink];
                }

                needShrink = true;
                break; // Сжимаем по одной оси за одну операцию remove
            }
        }

        // 5. Если сжатие одобрено — пересобираем массив
        if (needShrink) {
            makeArray(newCapacities);
        }
    }

    private boolean needsToRemake(int[] capacitiesToCheck) {
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

    private int getLinearIndex(int[] axises, int[] steps) {
        int linearIndex = 0;
        for (int i = 0; i < axises.length; i++){
            linearIndex += axises[i] * steps[i];
        }
        return linearIndex;
    }

    private int getFreeCellIndex(){
        for (int i = 0; i < this.array.length; i++) {
            if (this.array[i] == null) {
                return i;
            }
        }
        return -1;
    }

    private int getDimensionToExpand() {
        int dimensionToExpand = this.capacities.length - 1;
        for(int i = this.capacities.length - 2; i >= 0; i--) {
            if (capacities[i] < capacities[dimensionToExpand]) {
                dimensionToExpand = i;
            }
        }
        return dimensionToExpand;
    }

    private int getDimensionToShrink() {
        int dimensionToShrink = 0;
        for(int i = 0; i < this.capacities.length; i++) {
            if (capacities[i] > capacities[dimensionToShrink]) {
                dimensionToShrink = i;
            }
        }
        return dimensionToShrink;
    }

    private void recalculateCounts() {
        for (int i = 0; i < this.counts.length; i++) {
            this.counts[i] = 0;
        }

        for (int i = 0; i < this.array.length; i++) {
            if (this.array[i] != null) {
                int tempIndex = i;
                for (int dimension = 0; dimension < this.capacities.length; dimension++) {
                    int coordination = tempIndex / this.steps[dimension];
                    if (coordination + 1 > this.counts[dimension]) {
                        this.counts[dimension] = coordination + 1;
                    }
                    tempIndex %= this.steps[dimension];
                }
            }
        }
    }

    private int getTotalSize(int[] newCapacities) {
        int totalSize = 1;
        for (int capacity : newCapacities) {
            totalSize *= capacity;
        }
        return totalSize;
    }

    public int getTotalSize() {
        return getTotalSize(this.capacities);
    }
}
