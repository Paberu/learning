package PowerSet;

public class PowerSet_2 {

    public static PowerSet decartMultiply(PowerSet first, PowerSet second) {
        PowerSet result = new PowerSet();
        for (String key1 : first.values()) {
            for (String key2 : second.values()) {
                result.put(key1+","+key2);
            }
        }
        return result;
    }
}
