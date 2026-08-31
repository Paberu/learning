package utils;

import java.io.*;
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

    public static void generateFiles() {
        for (int i = 1; i <= 10; i++) {
            String filename = i + ".txt";
            try {
                File newFile = new File(filename);
                BufferedWriter bw = new BufferedWriter(new FileWriter(newFile));
                for (int j = 0; j < 3; j++) {
                    Random random = new Random();
                    bw.write(random.nextInt(100) + "");
                    bw.newLine();
                }
                bw.close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    public static int sumSomeIntFromFiles(int n1, int n2) {
        String filename1 = n1 + ".txt";
        String filename2 = n2 + ".txt";
        int sum = 0;
        try {
            BufferedReader br1 = new BufferedReader(new FileReader(n1 + ".txt"));
            BufferedReader br2 = new BufferedReader(new FileReader(n2 + ".txt"));
            String string = "";
            for (int i = 0; i < 3; i++){
                string = br1.readLine();
                /*if (string == null || string.equals("")) {
                    throw new IllegalArgumentException(filename1 + " повреждён или неполон");
                }*/
                sum += Integer.parseInt(string);
                string = br2.readLine();
                /*if (string == null || string.equals("")) {
                    throw new IllegalArgumentException(filename2 + " повреждён или неполон");
                }*/
                sum += Integer.parseInt(string);
            }
        } catch (FileNotFoundException fnfe) {
            throw new RuntimeException(fnfe);
        } catch (IOException ioe) {
             throw new RuntimeException(ioe);
        } catch (NumberFormatException nfe) {
            throw new RuntimeException(nfe);
        }
        return sum;
    }

    public static void main(String[] args) {
        // generateFiles();
        // System.out.println(sumSomeIntFromFiles(1, 2));
        System.out.println(sumSomeIntFromFiles(4, 3));
        System.out.println(sumSomeIntFromFiles(5, 9));
    }
}
