package NativeDictionary;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class NativeDictionary_3 {

    NativeDictionary<String> dict1;
    NativeDictionary<String> dict2;
    NativeDictionary<String> dict3;
    NativeDictionary<String> dict4;

    @BeforeEach
    void setUp() {
        dict1 = new NativeDictionary<String>(3, String.class);
        dict2 = new NativeDictionary<String>(7, String.class);
        dict3 = new NativeDictionary<String>(9, String.class);
        dict4 = new NativeDictionary<String>(10, String.class);

        dict1.put("First", "Java");
        dict1.put("Second", "Python");
        dict1.put("Third", "SQL");
    }

    @Test
    void testPut() {
        dict1.put("Third", "PHP");
        for (int i = 0; i < 3; i++) {
            assertNotEquals("SQL", dict1.values[i]);
        }
    }
}
