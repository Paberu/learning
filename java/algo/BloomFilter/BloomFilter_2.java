package BloomFilter;

public class BloomFilter_2 {
    public int filter_len;
    public byte[] filter;   // для возможности удаления я перехожу от массива битов к массиву байтов

    public BloomFilter_2(int f_len) {
        filter_len = f_len;
        filter = new byte[f_len];
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
