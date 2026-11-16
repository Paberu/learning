package NativeDictionary;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

public class NativeDictionary_3 {
    // Задача 4. Добавьте в этот класс три метода.
    // Сделайте тесты, проверяющие, как работают put(), is_key() и get():
    //- добавление значения по новому ключу и добавление значения по уже существующему ключу с проверками что записалось,
    //- проверка присутствующего и отсутствующего ключей,
    //- извлечение значения по существующему и отсутствующему ключу

    NativeDictionary<String> dict1;
    NativeDictionary_2<String> dict2;
    SortedDictionary<String> sortedDict;

    @BeforeEach
    void setUp() {
        dict1 = new NativeDictionary<String>(3, String.class);
        dict1.put("First", "Java");
        dict1.put("Second", "Python");
        dict1.put("Third", "SQL");

        dict2 = new NativeDictionary_2<String>(4);   // ключи длиной 4 бита: от 0 до 15

        sortedDict = new SortedDictionary<String>(String.class);
    }

    @Test
    void testPut() {
        assertEquals("SQL", dict1.get("Third"));
        dict1.put("Third", "PHP");
        assertEquals("PHP", dict1.get("Third"));
        assertTrue(dict1.isKey("Third"));
        assertEquals(3, countNotNull(dict1.values));
        for (int i = 0; i < 3; i++) {
            assertNotEquals("SQL", dict1.values[i]);
        }
    }

    private static int countNotNull(Object[] array) {
        int count = 0;
        for (Object value : array) {
            if (value != null)
                count++;
        }
        return count;
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

    @Test
    void testPutAndGet() {
        dict2.put(0L, "zero");
        dict2.put(15L, "fifteen");

        assertEquals("zero", dict2.get(0L));
        assertEquals("fifteen", dict2.get(15L));
        assertEquals(2, dict2.size());
    }

    @Test
    void testIsKeyInBitDict() {
        dict2.put(7L, "seven");

        assertTrue(dict2.isKey(7L));
        assertFalse(dict2.isKey(8L));
        assertNull(dict2.get(8L));
    }

    @Test
    void testPutExistingKeyInBitDict() {
        dict2.put(3L, "three");
        dict2.put(3L, "тройка");

        assertEquals("тройка", dict2.get(3L));
        assertEquals(1, dict2.size());
    }

    @Test
    void testRemoveInBitDict() {
        dict2.put(1L, "один");
        dict2.put(2L, "два");

        assertEquals("один", dict2.remove(1L));
        assertFalse(dict2.isKey(1L));
        assertNull(dict2.get(1L));
        assertEquals(1, dict2.size());
        assertNull(dict2.remove(1L));

        assertEquals("два", dict2.get(2L));
    }

    @Test
    void testPutNullValueInBitDict() {
        assertThrows(IllegalArgumentException.class, () -> dict2.put(1L, null));
    }

    @Test
    void testKeyOutOfRangeInBitDict() {
        assertThrows(IllegalArgumentException.class, () -> dict2.put(-1L, "минус один"));
        assertThrows(IllegalArgumentException.class, () -> dict2.put(16L, "шестнадцать"));
        assertThrows(IllegalArgumentException.class, () -> dict2.get(-1L));
        assertThrows(IllegalArgumentException.class, () -> dict2.isKey(16L));
        assertThrows(IllegalArgumentException.class, () -> dict2.remove(16L));
    }

    @Test
    void testKeyLengthInBitDict() {
        assertThrows(IllegalArgumentException.class, () -> new NativeDictionary_2<String>(0));
        assertThrows(IllegalArgumentException.class, () -> new NativeDictionary_2<String>(-1));
        assertThrows(IllegalArgumentException.class, () -> new NativeDictionary_2<String>(Long.SIZE + 1));
    }

    @Test
    void testSmallestTableInBitDict() {
        NativeDictionary_2<String> oneBit = new NativeDictionary_2<String>(1);

        oneBit.put(0L, "ноль");
        oneBit.put(1L, "один");

        assertEquals("ноль", oneBit.get(0L));
        assertEquals("один", oneBit.get(1L));
        assertEquals(2, oneBit.size());
        assertThrows(IllegalArgumentException.class, () -> oneBit.put(2L, "два"));
    }

    @Test
    void testGrowthKeepsAllKeysInBitDict() {
        NativeDictionary_2<String> dict = new NativeDictionary_2<String>(6);   // ключи 0..63
        for (long key = 0; key < 40; key++) {
            dict.put(key, "v" + key);   // таблица расширяется, коллизии разрешаются пробированием
        }

        assertEquals(40, dict.size());
        for (long key = 0; key < 40; key++) {
            assertEquals("v" + key, dict.get(key));
        }
    }

    @Test
    void testRemoveKeepsProbingChainInBitDict() {
        NativeDictionary_2<String> dict = new NativeDictionary_2<String>(8);   // ключи 0..255
        for (long key = 0; key < 200; key++) {
            dict.put(key, "v" + key);   // ключей больше, чем ячеек, так что коллизии и пробирование гарантированы
        }

        for (long key = 0; key < 200; key += 3) {   // удаляем каждого третьего
            assertEquals("v" + key, dict.remove(key));
        }

        for (long key = 0; key < 200; key++) {
            if (key % 3 == 0) {
                assertFalse(dict.isKey(key), "ключ " + key + " должен быть удалён");
                assertNull(dict.get(key));
            } else {
                assertTrue(dict.isKey(key), "ключ " + key + " потерялся после удаления соседей");
                assertEquals("v" + key, dict.get(key));
            }
        }
        assertEquals(133, dict.size());   // осталось 200 - 67
    }

    // -------------------- Задача 5: SortedDictionary (словарь на упорядоченном списке) --------------------

    @Test
    void testSortedPutAndGet() {
        sortedDict.put("b", "2");
        sortedDict.put("a", "1");
        sortedDict.put("c", "3");

        assertEquals("1", sortedDict.get("a"));
        assertEquals("2", sortedDict.get("b"));
        assertEquals("3", sortedDict.get("c"));
        assertEquals(3, sortedDict.values.count);
    }

    @Test
    void testSortedIsKeyAndGetAbsent() {
        sortedDict.put("b", "2");

        assertTrue(sortedDict.isKey("b"));
        assertFalse(sortedDict.isKey("a"));
        assertNull(sortedDict.get("a"));
    }

    @Test
    void testSortedPutExistingKey() {
        sortedDict.put("a", "1");
        sortedDict.put("a", "11");

        assertEquals("11", sortedDict.get("a"));
        assertEquals(1, sortedDict.slots.size());   // ключ не задвоился
        assertEquals(1, sortedDict.values.count);   // значение не задвоилось
    }

    @Test
    void testSortedRemove() {
        sortedDict.put("a", "1");
        sortedDict.put("b", "2");
        sortedDict.put("c", "3");

        assertEquals("2", sortedDict.remove("b"));
        assertFalse(sortedDict.isKey("b"));
        assertNull(sortedDict.get("b"));
        assertEquals(2, sortedDict.slots.size());
        assertEquals(2, sortedDict.values.count);

        assertNull(sortedDict.remove("z"));   // отсутствующий ключ

        // соседние пары не перепутались: ключ по-прежнему лежит под тем же индексом, что и его значение
        assertEquals("1", sortedDict.get("a"));
        assertEquals("3", sortedDict.get("c"));
    }

    @Test
    void testSortedSeveralKeysInMiddle() {
        sortedDict.put("m", "13");
        sortedDict.put("a", "1");
        sortedDict.put("z", "26");
        sortedDict.put("b", "2");
        sortedDict.put("y", "25");

        assertEquals("1", sortedDict.get("a"));
        assertEquals("2", sortedDict.get("b"));
        assertEquals("13", sortedDict.get("m"));
        assertEquals("25", sortedDict.get("y"));
        assertEquals("26", sortedDict.get("z"));
        assertEquals(5, sortedDict.slots.size());
        assertEquals(5, sortedDict.values.count);
    }

    @Test
    void testSortedKeysStaySortedAndPairedWithValues() {
        List<String> keys = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            keys.add("k" + i);
        }
        Collections.shuffle(keys, new Random(42));   // ключи приходят в произвольном порядке

        for (String key : keys) {
            sortedDict.put(key, "v" + key);
        }

        // значения не перепутались с ключами
        for (String key : keys) {
            assertEquals("v" + key, sortedDict.get(key));
        }
        assertEquals(keys.size(), sortedDict.slots.size());
        assertEquals(keys.size(), sortedDict.values.count);

        // и список ключей остался упорядоченным: индексы по возрастанию ключей строго возрастают
        List<String> sortedKeys = new ArrayList<>(keys);
        Collections.sort(sortedKeys);
        int previousIndex = -1;
        for (String key : sortedKeys) {
            int index = sortedDict.slots.find(key);
            assertTrue(index > previousIndex, "ключ " + key + " оказался не на своём месте");
            previousIndex = index;
        }
    }
}
