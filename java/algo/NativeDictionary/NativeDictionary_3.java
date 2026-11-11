package NativeDictionary;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class NativeDictionary_3 {
    // Задача 4. Добавьте в этот класс три метода.
    // Сделайте тесты, проверяющие, как работают put(), is_key() и get():
    //- добавление значения по новому ключу и добавление значения по уже существующему ключу с проверками что записалось,
    //- проверка присутствующего и отсутствующего ключей,
    //- извлечение значения по существующему и отсутствующему ключу

    NativeDictionary<String> dict1;

    @BeforeEach
    void setUp() {
        dict1 = new NativeDictionary<String>(3, String.class);

        dict1.put("First", "Java");
        dict1.put("Second", "Python");
        dict1.put("Third", "SQL");
    }

    @Test
    void testPut() {
        assertEquals("SQL", dict1.get("Third"));
        dict1.put("Third", "PHP");
        for (int i = 0; i < 3; i++) {
            assertNotEquals("SQL", dict1.values[i]);
        }
    }

    @Test
    void testPutInFullDict() {
        dict1.put("Fourth", "Ruby");
        assertEquals(6,dict1.size);
        assertTrue(dict1.isKey("Fourth"));
        assertEquals("Ruby", dict1.get("Fourth"));
    }

    @Test
    void testIsKey() {
        assertTrue(dict1.isKey("First"));
        assertFalse(dict1.isKey("Fourth"));
    }

    @Test
    void testGet() {
        assertEquals("Java", dict1.get("First"));
        assertNull(dict1.get("Fourth"));
    }

}
