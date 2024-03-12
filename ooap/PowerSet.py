from typing import Final
from HashTable import HashTable


class PowerSet(HashTable):

    # конструктор
    def __init__(self):
        super().__init__(29)

    # команды
    # корректировка HashTable - отказ от размещения имеющегося в множестве значения
    def put(self, value):
        index = self.get(value)
        if self.get_get_status == self.GET_ERR:
            self._inner[index] = value
            self._put_status = self.PUT_OK
            self._length += 1
        else:
            self._put_status = self.PUT_ERR

    # составные запросы
    def intersection(self, set2):
        inter_set = PowerSet()
        for each in self.__insides:
            if each is not None:
                for value in each:
                    if set2.get(value) == self.GET_OK:
                        inter_set.put(value)
        return inter_set

    def union(self, set2):
        union_set = self.__copy()
        for each in set2.__insides:
            if each is not None:
                for value in each:
                    union_set.put(value)
        return union_set

    def difference(self, set2):
        diff_set = PowerSet()
        for each in self.__insides:
            if each is not None:
                for value in each:
                    if not set2.get(value):
                        diff_set.put(value)
        return diff_set

    def issubset(self, set2):
        for each in set2.__insides:
            if each is not None:
                for value in each:
                    if not self.get(value):
                        return False
        return True

    # вспомогательная функция копирования множества
    def __copy(self):
        copy_set = PowerSet()
        for each in self.__insides:
            if each is not None:
                for value in each:
                    copy_set.put(value)
        return copy_set
