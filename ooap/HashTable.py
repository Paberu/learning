from typing import Final


class HashTable:

    HASH_FUN_NIL: Final = 0
    HASH_FUN_OK: Final = 1
    HASH_FUN_ERR: Final = 2
    SEEK_SLOT_NIL: Final = 0
    SEEK_SLOT_OK: Final = 1
    SEEK_SLOT_ERR: Final = 2
    PUT_NIL: Final = 0
    PUT_OK: Final = 1
    PUT_ERR: Final = 2
    FIND_NIL: Final = 0
    FIND_OK: Final = 1
    FIND_ERR: Final = 2

    def __init__(self, sz):
        self.size = sz
        self.inner = [None] * sz

        self._hash_fun_status = self.HASH_FUN_NIL
        self._seek_slot_status = self.SEEK_SLOT_NIL
        self._put_status = self.PUT_NIL
        self._find_status = self.FIND_NIL

    # запросы
    # предусловие: аргумент строковый
    # постусловие: получен результат работы хэш-суммы
    def hash_fun(self, value):
        sum_value = 0
        if isinstance(value, str):
            for letter in value:
                sum_value += ord(letter)
            self._hash_fun_status = self.HASH_FUN_OK
        else:
            self._hash_fun_status = self.HASH_FUN_ERR
        return sum_value % self.size

    # предусловие: аргумент строковый; указанный слот ничем не занят
    # постусловие: получен адрес ячейки для размещения значения
    def seek_slot(self, value):
        basic_index = self.hash_fun(value)
        slot = 0
        if self._hash_fun_status == self.HASH_FUN_OK and not self.inner[basic_index]:
            slot = basic_index
            self._seek_slot_status = self.SEEK_SLOT_OK
        else:
            self._seek_slot_status = self.SEEK_SLOT_ERR
        return slot

    # предусловие: аргумент строковый
    # постусловие: возвращает адрес ячейки, в которой находится данное значение
    def find(self, value):
        basic_index = self.hash_fun(value)
        if self._hash_fun_status == self.HASH_FUN_OK and self.inner[basic_index] == value:
            self._find_status = self.FIND_OK
        else:
            self._find_status = self.FIND_ERR
        return basic_index

    # команда
    # предусловие: аргумент строковый; указанный слот ничем не занят
    # постусловие: значение размещено в хэш-таблицу
    def put(self, value):
        index = self.seek_slot(value)
        if self._seek_slot_status == self.SEEK_SLOT_OK:
            self.inner[index] = value
            self._put_status = self.PUT_OK
        else:
            self._put_status = self.PUT_ERR

    #  запросы получения статусов
    def get_hash_fun_status(self):  # успешно; хэш не подсчитан
        return self._hash_fun_status

    def get_seek_slot_status(self):  # успешно; слот не выбран
        return self._seek_slot_status

    def get_put_status(self):  # успешно; не удалось поместить значение в таблицу
        return self._put_status

    def get_find_status(self):  # успешно; ничего не найдено
        return self._find_status
