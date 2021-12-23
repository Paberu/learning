import unittest
from HashTable import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash1 = HashTable(17, 3)

    def test_hash_fun(self):
        str_list = '''
Когда мы будем знакомиться с алгоритмами поиска, то узнаем, что в общем случае сложность поиска нужного элемента в упорядоченном массиве (когда есть возможность обращаться к произвольным элементам по индексу) можно снизить с O(n) до O(log n). Однако существуют структуры данных, которые ориентированы на максимально быстрый поиск нужной информации (проверку её наличия в хранилище), буквально за время O(1). Такие структуры называются хэш-таблицы.

Идея хэш-таблицы в том, что по значению содержимого i-го элемента таблицы мы можем быстро и однозначно определить сам индекс i (говорят - слот). Такое вычисление слота выполняет специальная хэш-функция.

Если диапазон значений, хранимых в таблице, не превышает её размер, то хэш-функция элементарна. Например, мы хотим хранить байты (значения от 0 до 255) в таблице размером 256 элемента. В таком случае хэш-функция f(x) = x : само значение элемента и есть его индекс в таблице. Мы просто смотрим, имеется ли значение N в таблице по индексу N.

Но идея хэш-таблиц в другом: мы хотим хранить значения потенциально очень широкого диапазона (например, строки) в таблице маленького размера (например, 128 элементов). При этом мы исходим из того, что и хранимые данные по своей уникальности примерно близки своим количеством размеру хэш-таблицы. Мы можем, например, суммировать байты каждой строки, брать остаток от деления суммы на 128, и таким образом получать уникальный индекс.

Большая проблема в том, что идеальную хэш-функцию придумать подчас очень трудно или невозможно. В нашем случае самые разные строки могут выдавать один и тот же слот -- такая ситуация называется коллизией. Решается эта проблема, во-первых, подбором оптимальной хэш-функции, которая минимизирует количество коллизий, и во-вторых, так называемым разрешением коллизий, когда несколько разных значений претендуют на один слот.
'''.split()
        result = [0]*17
        for every_str in str_list:
            index = self.hash1.hash_fun(every_str)
            result[index] += 1

        for i in range(len(result)):
            print(result[i])


unittest.main()
        
