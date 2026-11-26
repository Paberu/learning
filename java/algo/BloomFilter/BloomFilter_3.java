package BloomFilter;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class BloomFilter_3 {

    String str1;
    String str2;
    String str3;
    String str4;
    String str5;
    String str6;
    String str7;
    String str8;
    String str9;
    String str10;
    BloomFilter bloomFilter;

    @BeforeEach
    void setUp() {
        str1 = "0123456789";
        str2 = "1234567890";
        str3 = "2345678901";
        str4 = "3456789012";
        str5 = "4567890123";
        str6 = "5678901234";
        str7 = "6789012345";
        str8 = "7890123456";
        str9 = "8901234567";
        str10 = "9012345678";
        bloomFilter = new BloomFilter(32);
    }

    @Test
    void testBloom() {
        bloomFilter.add(str1);
        bloomFilter.add(str2);
        bloomFilter.add(str3);
        bloomFilter.add(str4);
        bloomFilter.add(str5);
        bloomFilter.add(str6);
        bloomFilter.add(str7);
        bloomFilter.add(str8);
        bloomFilter.add(str9);
        bloomFilter.add(str10);
        assertEquals(0b101000000000000010000000100000, bloomFilter.filter);
        assertFalse(bloomFilter.isValue("1029384756"));
        assertTrue(bloomFilter.isValue("0987654321"));      // ложноположительное срабатывание
        assertFalse(bloomFilter.isValue("0897867564534231"));
        assertFalse(bloomFilter.isValue("1111111111"));
        assertFalse(bloomFilter.isValue("0000000000"));
        assertFalse(bloomFilter.isValue("675849302"));
        assertFalse(bloomFilter.isValue("574839106"));
        assertTrue(bloomFilter.isValue("6789012345"));
        assertTrue(bloomFilter.isValue("7890123456"));
        assertTrue(bloomFilter.isValue("8901234567"));
    }

    @Test
    void recover(){
        System.out.println(BloomFilter_2.recoverValues(bloomFilter));
    }


}
