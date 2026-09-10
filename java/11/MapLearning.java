import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class MapLearning {

    private HashMap<Integer, String> hashMap;

    public MapLearning() {
         hashMap = new HashMap<>();
    }

    public void learnHashMap1() {
        for (int i = 0; i < 100; i++) {
            StringBuilder sb = new StringBuilder();
            Random random = new Random();
            for (int j = 0; j <= i; j++) {
                String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                int index = random.nextInt(alphabet.length());
                sb.append(alphabet.charAt(index));
            }
            String value = sb.toString();
            hashMap.put(i, value);
        }
        System.out.println(this.hashMap.size());

        for (int i = 0; i < 100; i++) {
            System.out.println(i + " " + hashMap.get(i));
        }

        for (int i = 0; i < 100; i++) {
            System.out.println(i + " " + hashMap.remove(i));
        }

        System.out.println(this.hashMap.size());
    }

    public int[] useHashMap2(int[] intValues, int frequency) {
        HashMap<Integer, Integer> countFrequency = new HashMap<>();
        for (int value : intValues) {
            countFrequency.merge(value, 1, Integer::sum);
        }
        countFrequency.values().removeIf(v -> v < frequency);
        return countFrequency.keySet().stream().mapToInt(Integer::intValue).toArray();
    }

    static void main() {
        MapLearning ml = new MapLearning();
        ml.learnHashMap1();

        int[] intValues = new int[100];
        Random random = new Random();
        for (int i = 0; i < 100; i++) {
            intValues[i] = random.nextInt(1,11);
        }
        int[] goalValues = ml.useHashMap2(intValues, 10);
        for (int i : goalValues) {
            System.out.println(i);
        }

    }
}
