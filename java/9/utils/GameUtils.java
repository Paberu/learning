package utils;

import java.util.Random;

public class GameUtils {

    // Как же сложно обращаться к алгоритмам, сам не знаю почему. Обдумывать различные АТД было проще, чем
    // перебирать словесные описания сортировок и выбирать, какая будет лучше. Мне нужно будет сортировать список
    // юнитов на поле по их скорости, а значит там будет немного, до 15 элементов в массиве.
    public static void sort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int current = array[i];
            int j = i - 1;

            // Пока текущий элемент меньше предыдущего каждый элемент будет сдвигаться на одну позицию вправо.
            while (j >= 0 && array[j] > current) {
                array[j + 1] = array[j];
                j--;
            }

            // Когда алгоритм придёт в начало массива или упрётся в элемент меньше его, тогда элемент и будет
            // вставлен в массив.
            array[j + 1] = current;
        }
    }

    public static int[] generate(int count, int bound) {
        int[] numbers = new int[count];
        Random random = new Random();

        for (int i = 0; i < numbers.length; i++){
            numbers[i] = random.nextInt(bound+1);
        }
        return numbers;
    }
}
