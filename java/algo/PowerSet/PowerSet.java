package PowerSet;

public class PowerSet {
    // Курс "Практика в программировании на АСД. Задание 10.
    // Задача 1. Создайте реализующий множество класс PowerSet... поэтому для внутреннего хранения множества можно взять
    // даже стандартный список. Попробуем.

    private int length;


    public PowerSet() {
        length = 0;
        // ваша реализация хранилища
    }

    public int size() {
        // количество элементов в множестве
        return length;
    }


    public void put(String value)
    {
        // всегда срабатывает
    }

    public boolean get(String value)
    {
        // возвращает true если value имеется в множестве,
        // иначе false
        return false;
    }

    public boolean remove(String value)
    {
        // возвращает true если value удалено
        // иначе false
        return false;
    }

    public PowerSet intersection(PowerSet set2)
    {
        // пересечение текущего множества и set2
        return null;
    }

    public PowerSet union(PowerSet set2)
    {
        // объединение текущего множества и set2
        return null;
    }

    public PowerSet difference(PowerSet set2)
    {
        // разница текущего множества и set2
        return null;
    }

    public boolean isSubset(PowerSet set2)
    {
        // возвращает true, если set2 есть
        // подмножество текущего множества,
        // иначе false
        return false;
    }

    public boolean equals(PowerSet set2)
    {
        // возвращает true,
        // если set2 равно текущему множеству,
        // иначе false
        return false;
    }

}
