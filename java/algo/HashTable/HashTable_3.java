package HashTable;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class HashTable_3 {
    // Курс "Практика в программировании на АСД. Задание 8.
    // Напишите тесты, которые проверяют работу этих четырёх методов.

    // Тесты публичных методов HashTable, DynamicHashTable и MultiHashTable.
    // Конструкторы не проверяются.

    HashTable empty;
    HashTable table;
    HashTable full;

    DynamicHashTable dynamic;
    DynamicHashTable dynamicSmall;

    MultiHashTable multi;
    HashTable_2 helper;

    @BeforeEach
    void setUp() {
        empty = new HashTable(5, 2);
        table = new HashTable(5, 2);

        full = new HashTable(3, 1);
        full.put("a");
        full.put("b");
        full.put("c");

        dynamic = new DynamicHashTable(3, 1);
        dynamicSmall = new DynamicHashTable(2, 1);

        multi = new MultiHashTable(5, 1, 2);
        helper = new HashTable_2();
    }

    @Test
    void testHashFunEmptyString() {
        assertEquals(0, empty.hashFun(""));
    }

    @Test
    void testHashFunOneChar() {
        assertEquals(97, empty.hashFun("a"));
    }

    @Test
    void testHashFunSeveralChars() {
        assertEquals(195, empty.hashFun("ab"));
    }

    @Test
    void testSeekSlotEmpty() {
        assertEquals(2, empty.seekSlot("a"));
        assertArrayEquals(new String[5], empty.slots);
    }

    @Test
    void testSeekSlotCollision() {
        assertEquals(2, table.put("a"));
        assertEquals(4, table.seekSlot("f"));
        assertEquals("a", table.slots[2]);
        assertNull(table.slots[4]);
    }

    @Test
    void testSeekSlotFull() {
        assertEquals(-1, full.seekSlot("d"));
    }

    @Test
    void testPutEmpty() {
        assertEquals(2, table.put("a"));
        assertEquals("a", table.slots[2]);
    }

    @Test
    void testPutCollision() {
        table.put("a");
        assertEquals(4, table.put("f"));
        assertEquals(1, table.put("k"));
        assertEquals("a", table.slots[2]);
        assertEquals("f", table.slots[4]);
        assertEquals("k", table.slots[1]);
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
        table.put("a");
        table.put("f");
        table.put("k");
        assertEquals(2, table.find("a"));
        assertEquals(4, table.find("f"));
        assertEquals(1, table.find("k"));
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
        assertEquals(1, full.find("a"));
        assertEquals(2, full.find("b"));
        assertEquals(0, full.find("c"));
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
        assertEquals(0, dynamicSmall.put("aa"));
        assertEquals(1, dynamicSmall.put("b"));
        assertEquals(0, dynamicSmall.put("c"));
        assertEquals(4, dynamicSmall.size);
        assertEquals("c", dynamicSmall.slots[0]);
        assertNull(dynamicSmall.slots[1]);
        assertEquals("aa", dynamicSmall.slots[2]);
        assertEquals("b", dynamicSmall.slots[3]);
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
        dynamicSmall.put("c");
        assertEquals(2, dynamicSmall.find("aa"));
        assertEquals(3, dynamicSmall.find("b"));
        assertEquals(0, dynamicSmall.find("c"));
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
        assertDoesNotThrow(() -> helper.ddos(empty));
    }
}
