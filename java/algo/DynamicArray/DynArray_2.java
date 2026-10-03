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

    // Чем я реально горжусь - это функцией поиска оси для расширения. Казалось бы, мелочь, но до чего приятно же. )))
    public static final int MINIMUM_CAPACITY = 4;   // для удобства тестирования, мне же принцип понять надо

    private T[] array;
    private int[] capacities;
    private int[] steps;
    private int[] counts;
    private int totalCount = 0;
    Class clazz;

    public DynArray_2(Class<T> clz, int dimensions, int... capacities) {
        if (dimensions != capacities.length) {
            throw new IllegalArgumentException("Размерность не соблюдается.");
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
            throw new IllegalArgumentException("Размерность не соблюдается.");
        }
        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < 0 || indexes[i] >= this.counts[i]) {
                throw new IndexOutOfBoundsException("Координаты выходят за границы массива.");
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
            throw new IllegalArgumentException("Размерность не соблюдается.");
        }

        int targetLinearIndex = getLinearIndex(indexes, this.steps);
        if (targetLinearIndex < 0 || targetLinearIndex > this.totalCount) {
            throw new IndexOutOfBoundsException("Координаты выходят за границы массива.");
        }

        if (this.totalCount >= this.array.length) {
            int dimToExpand = getDimensionToExpand();
            int[] newCapacities = this.capacities.clone();
            newCapacities[dimToExpand] *= 2;

            makeArray(newCapacities);
            targetLinearIndex = getLinearIndex(indexes, this.steps);
        }

        if (this.totalCount - targetLinearIndex > 0) {
            System.arraycopy(this.array, targetLinearIndex, this.array, targetLinearIndex + 1, this.totalCount - targetLinearIndex);
        }

        this.array[targetLinearIndex] = itm;
        this.totalCount++;

        recalculateCounts();
    }

    public void remove(int... indexes) {
        if (indexes.length != this.capacities.length) {
            throw new IllegalArgumentException("Размерность не соблюдается.");
        }

        for (int i = 0; i < indexes.length; i++) {
            if (indexes[i] < 0 || indexes[i] >= this.counts[i]) {
                throw new IndexOutOfBoundsException("Координаты выходят за границы массива.");
            }
        }

        int targetLinearIndex = getLinearIndex(indexes, this.steps);

        int elementsToShift = this.totalCount - targetLinearIndex - 1;
        if (elementsToShift > 0) {              // на случай, если удалили последний элемент, то ничего сдвигать не надо
            System.arraycopy(this.array, targetLinearIndex + 1, this.array, targetLinearIndex, elementsToShift);
        }

        this.array[this.totalCount - 1] = null;
        this.totalCount--;

        recalculateCounts();

        boolean needsShrinking = false;
        int[] newCapacities = this.capacities.clone();

        for (int i = 0; i < this.capacities.length; i++) {
            if (this.counts[i] < (double) this.capacities[i] / 2 && this.capacities[i] > MINIMUM_CAPACITY) {
                int shrunkCapacity = (int) (newCapacities[i] / 1.5);
                newCapacities[i] = Math.max(shrunkCapacity, MINIMUM_CAPACITY);

                if (newCapacities[i] < this.counts[i]) {
                    newCapacities[i] = this.counts[i];
                }
                needsShrinking = true;
                break;
            }
        }

        if (needsShrinking) {
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

    private void recalculateCounts() {
        for (int i = 0; i < this.counts.length; i++) {
            this.counts[i] = 0;
        }

        for (int i = 0; i < totalCount; i++) {
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

/* Рефлексия.
Рекомендация: Первоначально проверяем, если длины этих списков не равны, то выбрасываем исключение ( хотя в целом это всегда плохой подход).
Далее в цикле пробегаемся синхронно по элементам каждого из списков, и их сумму добавляем в хвост списка-результата. В заголовке цикла достаточно проверять только один список (не завершился ли он), так как длины равны.

Я не исключение выбрасываю, я возвращаю пустой список, мол, если Вы не удосужились привести списки во взаимооднозначное соотвествие, почему я должен нянькой за Вами бегать.
Пользователь не обязан догадываться, как устроена работа метода: либо организуй нормальное ведение javadocs-комментариев, либо включаем
правило, едва не похоронившее рынок браузеров: будь строг к себе и милостив к конечному пользователю.

Как бы я реализовал "правило милости" (термин мой, поэтому в кавычках): пока node1 и node2 оба не null, мы заполняем новый
список суммами значений их "параллельных" узлов. Как только один из узлов null, мы берём остатки другого списка, и по одной
дописываем их к новому. Если же списки обязаны быть одной длины, то во-первых, это должно быть указано в javadocs-комментарии,
а во-вторых, надо бросать исключение с хорошим описаниемю
 */