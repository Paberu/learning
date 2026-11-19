package PowerSet;

import HashTable.HashTable;

import java.util.ArrayList;
import java.util.HashMap;

public class PowerSet_2 {

    public static PowerSet decartMultiply(PowerSet first, PowerSet second) {
        PowerSet result = new PowerSet();
        for (String key1 : first.values()) {
            for (String key2 : second.values()) {
                result.put(key1+","+key2);
            }
        }
        return result;
    }

    public static PowerSet multiIntersect(ArrayList<PowerSet> listOfSets) {
        if (listOfSets == null || listOfSets.isEmpty()) {
            return new PowerSet();
        }
        PowerSet result = listOfSets.get(0);
        for (int i = 1; i < listOfSets.size(); i++) {
            result = result.intersection(listOfSets.get(i));
        }
        return result;
    }

}

class Bag {

    private int length;
    private HashTable hashTable;

    public Bag() {
        length = 0;
        hashTable = new HashTable(20000, 13);
    }

    public int size() {
        return length;
    }

    public ArrayList<String> values() {
        return hashTable.values();
    }

    public void put(String value) {
        int index = hashTable.put(value);
        if (index != -1)
            length++;
    }

    public boolean get(String value) {
        int index = hashTable.find(value);
        return index != -1;
    }

    public boolean remove(String value) {
        int index = hashTable.remove(value);
        if (index == -1)
            return false;
        length--;
        return true;
    }

    public HashMap<String, Integer> getAll() {
        HashMap<String, Integer> values = new HashMap<>();
        for (String value : hashTable.values()) {
            values.merge(value, 1, Integer::sum);
        }
        return values;
    }

}

// Рефлексия. **Рекомендации по решению задач задания 8.**
/*
 3. **Динамическая хэш-таблица**.
 Подобную задачку уже мы делали. Напомню, используем композицию и храним таблицу в динамическом массиве, и в него надо
 добавить геттер размера буфера и явный вызов расширения размера (когда например таблица заполнена на 80%).
 А когда динамический массив реаллоцируется, конечно надо будет перераспределять элементы хэш-таблицы.
*/

/*
Здесь, каюсь, случилось повторение ошибки, которая преследовала меня на протяжении всего курса. Меня очень привлекла
идея описать изменение хранилища прямо в коде, поэтому поле хранилища - это снова массив, а в put - снова изменение
режима, и, что самое плохое, даже не подумал, когда я делаю ресайз. А именно - в момент, когда поиск индекса дал -1, то
есть, когда добавление нового элемента стоит чистейшего O(n) и всё равно ведёт к неудаче. Почему не задумался о ресайзе
на моменте заполненности в 80%? Потому что в динамическом массиве ресайзил при полной заполненности. Иногда кураж
исследователя натыкается на синдром отличника (лучше назвать его болезнью "хорошего мальчика) и сдаётся. Мы на предыдущем
урове ресайзили при 100% заполненности, значит и здесь так же. И именно в два раза. А почему не на 80%, и не в 1,6 раза?
Хотя бы ради эксперимента. Интересные вещи вскрываются...
*/

/*
 4. **ddos хэш-таблицы и соль**.
 Если вы сделали статическую соль, это не очень здорово, поскольку одинаковые значения будут хэшироваться в один и тот
 же результат.
 Лучше добавлять короткую динамическую соль к значениям, к хэшу добавлять небольшие случайные значения и т.п. А храним
 в таблице, соответственно, сущность с двумя полями: значение и соль.
*/

/*
Загуглил про соль и врубил тупую инициализацию встроенным в JDK рандомайзером. При каждом создании новой хэш-таблицы
соответственно заново генерится и соль. Я сам не представляю, что там будет, поэтому предсказать, какой окажется хэш
у того или иного значения невозможно. Возможно, соль на каждое значение разумнее, чем случайная соль на весь класс, но
как будто бы и этого хватает. Хотя, если погуглить про работу SHA-256 может оказаться, что там даже рандомайзер завязан
на работу атомных часов на PCI-плате или на алгебраическое описание карты звёздного неба в текущий момент времени (да,
общался с безопасниками, наслушался и не такого :)).
*/