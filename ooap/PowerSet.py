from typing import Final


class PowerSet:

    HASH_NIL: Final = 0
    HASH_OK: Final = 1
    HASH_ERR: Final = 2
    GET_NIL: Final = 0
    GET_OK: Final = 1
    GET_ERR: Final = 2
    PUT_NIL: Final = 0
    PUT_OK: Final = 1
    PUT_ERR: Final = 2
    REMOVE_NIL: Final = 0
    REMOVE_OK: Final = 1
    REMOVE_ERR: Final = 2

    # конструктор
    def __init__(self):
        self.__inner_size = 29
        self.__insides = [None] * self.__inner_size
        self.__length = 0

        self.__hash_status = self.HASH_NIL
        self.__get_status = self.GET_NIL
        self.__put_status = self.PUT_NIL
        self.__remove_status = self.REMOVE_NIL

    # размер множества
    def size(self):
        return self.__length

    # запросы
    # вспомогательная private-функция для расчёта хэша
    # предусловие: аргумент - это строка или число
    # постусловие: получен кэш, он же индекс, для размещения во внутреннее хранилище
    def __hash_fun(self, value):
        sum_value = 0
        if isinstance(value, str):
            for letter in value:
                sum_value += ord(letter)
            self.__hash_status = self.HASH_OK
        elif isinstance(value, int):
            sum_value = value
            self.__hash_status = self.HASH_OK
        else:
            self.__hash_status = self.HASH_ERR
        return sum_value % self.__inner_size

    # предусловие: аргумент - это строка или число
    # постусловие:
    def get(self, value):
        index = self.__hash_fun(value)
        if self.__insides[index] is not None and value in self.__insides[index]:
            self.__get_status = self.GET_OK
        else:
            self.__get_status = self.GET_ERR
        return self.__get_status == self.GET_OK

    # команды
    # предусловие: аргумент - это строка или число
    # постусловие: значение помещено в множество при условии, что его там уже не было
    def put(self, value):
        index = self.__hash_fun(value)
        if self.__hash_status == self.HASH_ERR:
            self.__put_status = self.PUT_ERR
        elif self.__insides[index] is None:
            self.__insides[index] = [value]
            self.__length += 1
            self.__put_status = self.PUT_OK
        else:
            if value not in self.__insides[index]:
                self.__insides[index].append(value)
                self.__length += 1
                self.__put_status = self.PUT_OK
            else:
                self.__put_status = self.PUT_ERR

    # предусловие: аргумент - это строка или число
    # постусловие: значение удалено из множества при условии, что оно там было
    def remove(self, value):
        index = self.__hash_fun(value)
        if self.__hash_status == self.HASH_OK and self.__insides[index] is not None and value in self.__insides[index]:
            self.__insides[index].remove(value)
            self.__length -= 1
            self.__remove_status = self.REMOVE_OK
        else:
            self.__remove_status = self.REMOVE_ERR

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

    # запросы на получение статусов выполнения public-функций
    def get_get_status(self):
        return self.__get_status

    def get_put_status(self):
        return self.__put_status

    def get_remove_status(self):
        return self.__remove_status
