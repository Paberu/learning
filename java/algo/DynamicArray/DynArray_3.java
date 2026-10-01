package DynamicArray;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class DynArray_3 {
    DynArray<Integer> dynArray;
    DynArray<Integer> dynArray2;

    @BeforeEach
    void setUp(){
        dynArray = new DynArray<Integer>(Integer.class);
        for (int i = 0; i < 14; i++) {
            dynArray.append(i*2);
        }
        dynArray2 = new DynArray<Integer>(Integer.class);
        for (int i = 0; i < 35; i++) {
            dynArray2.append(i*2);
        }
    }

    // Курс "Практика в программировании на АСД. Задание 3.
    // Задача 5. Напишите тесты, проверяющие работу методов Insert() и Remove():

    //-- вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);
    @Test
    void testInsertLight() {
        assertEquals(16, dynArray.capacity);
        assertEquals(14, dynArray.count);
        dynArray.insert(17, 5);
        assertEquals(16, dynArray.capacity);
        assertEquals(15, dynArray.count);
    }

    //-- вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);
    @Test
    void testInsertHeavy() {
        assertEquals(16, dynArray.capacity);
        assertEquals(14, dynArray.count);
        dynArray.insert(17, 5);
        dynArray.insert(19, 8);
        assertEquals(16, dynArray.capacity);
        assertEquals(16, dynArray.count);
        dynArray.insert(21, 11);
        assertEquals(32, dynArray.capacity);
        assertEquals(17, dynArray.count);
    }

    //-- попытка вставки элемента в недопустимую позицию;
    @Test
    void testInsertWrong() {
        assertEquals(16, dynArray.capacity);
        assertEquals(14, dynArray.count);
        assertThrows(IndexOutOfBoundsException.class, () -> dynArray.insert(17, 16));
        assertEquals(16, dynArray.capacity);
        assertEquals(14, dynArray.count);
    }

    //-- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);
    @Test
    void testRemoveLight() {
        assertEquals(64, dynArray2.capacity);
        assertEquals(35, dynArray2.count);
        dynArray2.remove(0);
        dynArray2.remove(1);
        assertEquals(64, dynArray2.capacity);
        assertEquals(33, dynArray2.count);
    }

    //-- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);
    @Test
    void testRemoveHeavy() {
        assertEquals(64, dynArray2.capacity);
        assertEquals(35, dynArray2.count);
        dynArray2.remove(0);
        dynArray2.remove(1);
        dynArray2.remove(2);
        dynArray2.remove(3);
        dynArray2.remove(4);
        dynArray2.remove(5);
        assertEquals(42, dynArray2.capacity);
        assertEquals(29, dynArray2.count);
    }

    //-- попытка удаления элемента в недопустимой позиции.
    @Test
    void testRemoveWrong() {
        assertEquals(64, dynArray2.capacity);
        assertEquals(35, dynArray2.count);
        assertThrows(IndexOutOfBoundsException.class, () -> dynArray.remove(36));
        assertEquals(64, dynArray2.capacity);
        assertEquals(35, dynArray2.count);
    }
}
