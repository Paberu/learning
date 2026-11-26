package BloomFilter;


// Задание 3. Реализуйте фильтр Блюма, предусматривающий удаление элементов (стандартный фильтр Блюма удаление не
// поддерживает)
public class BloomFilter_2 {
    public int filter_len;
    public byte[] filter;   // для возможности удаления я перехожу от массива битов к массиву байтов (счётчики)

    public BloomFilter_2(int f_len) {
        filter_len = f_len;
        filter = new byte[f_len];
    }

    public int hash(String str1, int salt) {
        int code = 0;
        for (int i = 0; i < str1.length(); i++) {
            code = (code * salt + str1.charAt(i)) % filter_len;
        }
        return code;
    }

    public void add(String str1) {
        // добавляем строку str1 в фильтр
        int position1 = hash(str1, 17);
        int position2 = hash(str1, 223);
        filter[position1] += 1;
        filter[position2] += 1;
    }

    public boolean isValue(String str1) {
        // проверка, имеется ли строка str1 в фильтре
        int position1 = hash(str1, 17);
        int position2 = hash(str1, 223);
        return filter[position1] != 0 && filter[position2] != 0;
    }

    // Иронично в этой ситуации то, что при имеющихся 10 строках из задания в исходном фильтре заполнено не так уж
    // много битов: 0b101000000000000010000000100000, а именно - 4. И мне удалось поймать ложноположительное срабатывание
    // на строке "0987654321". То есть, фильтр решит, что она есть, и удалит её, понизив счётчики. А если с упорством,
    // достойным лучшего применения, пытаться удалять эту строку из фильтра несколько раз, то может оказаться, что
    // байты в указанных местах уже упали до нуля, то есть проблема та же самая, что и в массиве битов.
    // В свою защиту скажу следующее: стандартный фильтр Блума даёт вероятностную оценку наличия данных - их точно нет
    // или они скорее всего есть, но это не точно. Мой фильтр Блума даёт некую количественную защиту от неверного
    // удаления: скорее всего защитит, но вообще без гарантий с моей стороны.
    public boolean remove(String str1) {
        int position1 = hash(str1, 17);
        int position2 = hash(str1, 223);
        if (filter[position1] == 0 || filter[position2] == 0)
            return false;
        filter[position1]--;
        filter[position2]--;
        return true;
    }

    // Сложность решения по времени - О(1). Идёт побитное логическое или, сработает молниеносно.
    // Сложность решения по пространству - О(1). Создаётся один новый фильтр Блюма.
    // Чем выше заполненность фильтра, тем выше вероятность ложноположительного результата. Мы объединяем два
    // фильтра, следовательно и вероятность ложных анализов растёт.
    public BloomFilter mergeBloomFilters(BloomFilter bf1, BloomFilter bf2) {
        BloomFilter unitedFilter = new BloomFilter(bf1.filter_len);
        unitedFilter.filter = bf1.filter | bf2.filter;
        return unitedFilter;
    }
}
