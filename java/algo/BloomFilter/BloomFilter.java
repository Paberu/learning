package BloomFilter;

public class BloomFilter {
    public int filter_len;
    public int filter;

    public BloomFilter(int f_len) {
        if (f_len <= 0 || f_len > 32) {
            throw new IllegalArgumentException("По условию задачи в качестве фильтра берётся 32-разрядное число.");
        }
        filter_len = f_len;
        filter = 0;
        // создаём битовый массив длиной f_len ...
    }

    // хэш-функции
    public int hash1(String str1) {
        // 17
        int code = 0;
        for (int i = 0; i < str1.length(); i++) {
            code = (code * 17 + str1.charAt(i)) % filter_len;
        }
        return code;
    }

    public int hash2(String str1) {
        // 223
        int code = 0;
        for (int i = 0; i < str1.length(); i++) {
            code = (code * 223 + str1.charAt(i)) % filter_len;
        }
        return code;
    }

    public void add(String str1) {
        // добавляем строку str1 в фильтр
        int position1 = hash1(str1);
        int position2 = hash2(str1);
        // хорошо, что эти операции у меня уже есть со времён побитовой работы с данными на Python
        filter |= 1 << position1;
        filter |= 1 << position2;
        // а раньше люди напрямую со всеми данными работали
    }

    public boolean isValue(String str1) {
        // проверка, имеется ли строка str1 в фильтре
        int position1 = hash1(str1);
        int position2 = hash2(str1);
        int mask = 0 | (1 << position1) | (1 << position2);
        int result = filter & mask;    // у фильтра единицы как минимум в тех же позициях, что и в маске
        return mask == result;          // поэтому маска и результат совпадут
    }
}