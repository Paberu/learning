package HashTable;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class HashTable_3 {
    // Курс "Практика в программировании на АСД. Задание 8.
    // Напишите тесты, которые проверяют работу этих четырёх методов.
    HashTable empty;
    HashTable table;
    HashTable full;

    DynamicHashTable dynamic;
    DynamicHashTable dynamicSmall;

    MultiHashTable multi;
    HashTable_2 helper;

    @BeforeEach
    void setUp() {
        empty = new HashTable(5, 3);
        table = new HashTable(5, 3);

        full = new HashTable(3, 1);
        full.put("a");
        full.put("b");
        full.put("c");

        dynamic = new DynamicHashTable(3, 1);
        dynamicSmall = new DynamicHashTable(3, 1);

        multi = new MultiHashTable(5, 1, 2);
        helper = new HashTable_2();
    }

    @Test
    void testHashFunEmptyString() {
        assertEquals(empty.salt, empty.hashFun(""));
    }

    @Test
    void testHashFunOneChar() {
        int hash = empty.hashFun("a");
        assertEquals(hash, empty.hashFun("a"));
        assertTrue(hash >= 0);
    }

    @Test
    void testHashFunSeveralChars() {
        assertEquals(empty.hashFun("ab"), empty.hashFun("ab"));
        assertNotEquals(empty.hashFun("ab"), empty.hashFun("ba"));
    }

    @Test
    void testSeekSlotEmpty() {
        assertEquals(empty.hashFun("a") % empty.size, empty.seekSlot("a"));
        assertArrayEquals(new String[5], empty.slots);
    }

    @Test
    void testSeekSlotCollision() {
        int index = table.put("a");
        String other = keyInBucket(table, table.hashFun("a") % table.size);
        int probed = (index + table.step) % table.size;
        assertEquals(probed, table.seekSlot(other));
        assertEquals("a", table.slots[index]);
        assertNull(table.slots[probed]);
    }

    @Test
    void testSeekSlotFull() {
        assertEquals(-1, full.seekSlot("d"));
    }

    @Test
    void testPutEmpty() {
        int index = table.put("a");
        assertEquals(table.hashFun("a") % table.size, index);
        assertEquals("a", table.slots[index]);
    }

    @Test
    void testPutCollision() {
        int first = table.put("a");
        int bucket = table.hashFun("a") % table.size;
        String secondKey = keyInBucket(table, bucket);
        String thirdKey = keyInBucket(table, bucket, secondKey);
        int second = table.put(secondKey);
        int third = table.put(thirdKey);
        assertEquals((first + table.step) % table.size, second);
        assertEquals((second + table.step) % table.size, third);
        assertEquals("a", table.slots[first]);
        assertEquals(secondKey, table.slots[second]);
        assertEquals(thirdKey, table.slots[third]);
    }

    @Test
    void testPutFull() {
        String[] before = full.slots.clone();
        assertEquals(-1, full.put("d"));
        assertArrayEquals(before, full.slots);
    }

    @Test
    void testFindEmpty() {
        assertEquals(-1, empty.find("a"));
    }

    @Test
    void testFindPresent() {
        int a = table.put("a");
        int bucket = table.hashFun("a") % table.size;
        String secondKey = keyInBucket(table, bucket);
        String thirdKey = keyInBucket(table, bucket, secondKey);
        int second = table.put(secondKey);
        int third = table.put(thirdKey);
        assertEquals(a, table.find("a"));
        assertEquals(second, table.find(secondKey));
        assertEquals(third, table.find(thirdKey));
    }

    @Test
    void testFindAbsentStopsAtEmptySlot() {
        table.put("a");
        table.put("f");
        table.put("k");
        assertEquals(-1, table.find("ab"));
        assertEquals(-1, table.find("z"));
    }

    @Test
    void testFindInFullTable() {
        assertEquals(indexOf(full, "a"), full.find("a"));
        assertEquals(indexOf(full, "b"), full.find("b"));
        assertEquals(indexOf(full, "c"), full.find("c"));
        assertEquals(-1, full.find("d"));
    }

    @Test
    void testDynamicHashFun() {
        assertEquals(0, dynamic.hashFun(""));
        assertEquals(97, dynamic.hashFun("a"));
        assertEquals(195, dynamic.hashFun("ab"));
    }

    @Test
    void testDynamicSeekSlotEmpty() {
        assertEquals(1, dynamic.seekSlot("a"));
        assertArrayEquals(new String[3], dynamic.slots);
    }

    @Test
    void testDynamicSeekSlotFull() {
        dynamic.put("a");
        dynamic.put("b");
        dynamic.put("c");
        assertEquals(-1, dynamic.seekSlot("d"));
        assertEquals(3, dynamic.size);
    }

    @Test
    void testDynamicPutWithoutResize() {
        assertEquals(1, dynamic.put("a"));
        assertEquals(2, dynamic.put("b"));
        assertEquals(0, dynamic.put("c"));
        assertEquals(3, dynamic.size);
        assertEquals("c", dynamic.slots[0]);
        assertEquals("a", dynamic.slots[1]);
        assertEquals("b", dynamic.slots[2]);
    }

    @Test
    void testDynamicPutResizesAndRehashes() {
        dynamic.put("a");
        dynamic.put("b");
        dynamic.put("c");
        assertEquals(4, dynamic.put("d"));
        assertEquals(6, dynamic.size);
        assertNull(dynamic.slots[0]);
        assertEquals("a", dynamic.slots[1]);
        assertEquals("b", dynamic.slots[2]);
        assertEquals("c", dynamic.slots[3]);
        assertEquals("d", dynamic.slots[4]);
        assertNull(dynamic.slots[5]);
    }

    @Test
    void testDynamicPutRehashesWithCollision() {
        assertEquals(2, dynamicSmall.put("aa"));
        assertEquals(0, dynamicSmall.put("b"));
        assertEquals(1, dynamicSmall.put("a"));
        assertEquals(4, dynamicSmall.put("c"));
        assertEquals(6, dynamicSmall.size);
        assertNull(dynamicSmall.slots[0]);
        assertEquals("a", dynamicSmall.slots[1]);
        assertEquals("b", dynamicSmall.slots[2]);
        assertEquals("aa", dynamicSmall.slots[3]);
        assertEquals("c", dynamicSmall.slots[4]);
        assertNull(dynamicSmall.slots[5]);
    }

    @Test
    void testDynamicFind() {
        dynamic.put("a");
        dynamic.put("b");
        dynamic.put("c");
        dynamic.put("d");
        assertEquals(1, dynamic.find("a"));
        assertEquals(2, dynamic.find("b"));
        assertEquals(3, dynamic.find("c"));
        assertEquals(4, dynamic.find("d"));
        assertEquals(-1, dynamic.find("z"));
    }

    @Test
    void testDynamicFindAfterCollisionResize() {
        dynamicSmall.put("aa");
        dynamicSmall.put("b");
        dynamicSmall.put("a");
        dynamicSmall.put("c");
        assertEquals(3, dynamicSmall.find("aa"));
        assertEquals(2, dynamicSmall.find("b"));
        assertEquals(1, dynamicSmall.find("a"));
        assertEquals(4, dynamicSmall.find("c"));
        assertEquals(-1, dynamicSmall.find("d"));
    }

    @Test
    void testHashFunK() {
        assertEquals(131, multi.hashFunK("a", 0));
        assertEquals(233, multi.hashFunK("a", 1));
        assertEquals(246, multi.hashFunK("ab", 0));
        assertEquals(448, multi.hashFunK("ab", 1));
        assertEquals(621, multi.hashFunK("a", 5));
    }

    @Test
    void testMultiSeekSlotUsesFirstFreeHash() {
        assertEquals(1, multi.seekSlot("a"));
        assertArrayEquals(new String[5], multi.slots);
        multi.put("a");
        assertEquals(3, multi.seekSlot("ab"));
    }

    @Test
    void testMultiSeekSlotProbesWhenHashesAreTaken() {
        multi.put("a");
        multi.put("ab");
        multi.put("b");
        assertEquals(4, multi.seekSlot("c"));
    }

    @Test
    void testMultiSeekSlotFull() {
        multi.put("a");
        multi.put("ab");
        multi.put("b");
        multi.put("c");
        multi.put("d");
        assertEquals(-1, multi.seekSlot("e"));
    }

    @Test
    void testMultiPut() {
        assertEquals(1, multi.put("a"));
        assertEquals(3, multi.put("ab"));
        assertEquals(2, multi.put("b"));
        assertEquals(4, multi.put("c"));
        assertEquals(0, multi.put("d"));
        assertArrayEquals(new String[]{"d", "a", "b", "ab", "c"}, multi.slots);
    }

    @Test
    void testMultiPutFull() {
        multi.put("a");
        multi.put("ab");
        multi.put("b");
        multi.put("c");
        multi.put("d");
        String[] before = multi.slots.clone();
        assertEquals(-1, multi.put("e"));
        assertArrayEquals(before, multi.slots);
    }

    @Test
    void testMultiFind() {
        multi.put("a");
        multi.put("ab");
        multi.put("b");
        multi.put("c");
        multi.put("d");
        assertEquals(1, multi.find("a"));
        assertEquals(3, multi.find("ab"));
        assertEquals(2, multi.find("b"));
        assertEquals(4, multi.find("c"));
        assertEquals(0, multi.find("d"));
        assertEquals(-1, multi.find("z"));
        assertEquals(-1, multi.find("hello"));
    }

    @Test
    void testMultiFindEmpty() {
        assertEquals(-1, multi.find("a"));
    }

    @Test
    void testDdos() {
        helper.ddos(empty);
        int bucket = rawSum(empty.slots[0]) % empty.size;
        for (String slot : empty.slots) {
            assertNotNull(slot);
            assertEquals(bucket, rawSum(slot) % empty.size);
        }
        assertNotEquals(empty.hashFun("ab"), empty.hashFun("ba"));
    }

    private int rawSum(String value) {
        int hash = 0;
        for (int i = 0; i < value.length(); i++)
            hash += value.charAt(i);
        return hash;
    }

    private int indexOf(HashTable ht, String value) {
        for (int i = 0; i < ht.slots.length; i++) {
            if (value.equals(ht.slots[i]))
                return i;
        }
        return -1;
    }

    private String keyInBucket(HashTable ht, int bucket, String... excluded) {
        for (int i = 0; i < 20000; i++) {
            String candidate = "k" + i;
            if (ht.hashFun(candidate) % ht.size != bucket)
                continue;
            boolean used = false;
            for (String excludedKey : excluded) {
                if (candidate.equals(excludedKey)) {
                    used = true;
                    break;
                }
            }
            if (!used)
                return candidate;
        }
        fail("Не удалось подобрать ключ для корзины " + bucket);
        return null;
    }
}
