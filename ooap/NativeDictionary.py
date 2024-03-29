from typing import Final


class NativeDictionary:

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

    #  конструктор
    def __init__(self, sz):

        self.__size = sz
        self.__step = 3
        while self.__size % self.__step == 0:
            self.__step += 2
        self.__slots = [None] * self.__size
        self.__values = [None] * self.__size

        self.__hash_status = self.HASH_NIL
        self.__get_status = self.GET_NIL
        self.__put_status = self.PUT_NIL
        self.__remove_status = self.REMOVE_NIL

    # запросы
    # предусловие: строковое значение ключа
    # постусловие: получено значение или решение, что по этому ключу ничего нет
    def get(self, key):
        basic_key_hash = self.__hash_fun(key)
        if self.__hash_status == self.HASH_OK and self.__slots[basic_key_hash] == key:
            self.__get_status = self.GET_OK
            return self.__values[basic_key_hash]
        elif self.__hash_status == self.HASH_OK:
            key_hash = self.__increase_key_hash(basic_key_hash)
            while key_hash != basic_key_hash:
                if self.__slots[key_hash] == key:
                    self.__get_status = self.GET_OK
                    return self.__values[key_hash]
                else:
                    key_hash = self.__increase_key_hash(key_hash)
        self.__get_status = self.GET_ERR

    # предусловие: строковое значение ключа
    # постусловие: получен ответ, является ключ ключом или нет
    def is_key(self, key):
        self.get(key)
        return self.__get_status == self.GET_OK

    # команды
    # предусловие: строковое значение ключа
    # постусловие: ключ и значение размещены в словаре или произошла коллизия
    def put(self, key, value):
        basic_key_hash = self.__hash_fun(key)
        if self.__slots[basic_key_hash] in (key, None):  # выглядит достаточно по-уродски, просто из-за отсутствия do-while
            self.__write_into_dict(basic_key_hash, key, value)
            self.__put_status = self.PUT_OK
        else:
            key_hash = self.__increase_key_hash(basic_key_hash)
            while key_hash != basic_key_hash:
                if self.__slots[key_hash] in (key, None):
                    self.__write_into_dict(key_hash, key, value)
                    self.__put_status = self.PUT_OK
                    break
                else:
                    key_hash = self.__increase_key_hash(key_hash)
            else:
                self.__put_status = self.PUT_ERR  # коллизия

    # предусловие: строковое значение ключа
    # постусловие: ключ и соответсвующее значение удалены (на их прежнем месте теперь None)
    def remove(self, key):
        if self.is_key(key):
            key_hash = self.__hash_fun(key)
            while True:
                if self.__slots[key_hash] == key:
                    self.__slots[key_hash] = None
                    self.__values[key_hash] = None
                    self.__remove_status = self.REMOVE_OK
                    break
                else:
                    key_hash = self.__increase_key_hash(key_hash)
        else:
            self.__remove_status = self.REMOVE_ERR

    # вспомогательные функции
    # предусловие: строковое значение ключа
    # постусловие: получен номер ячейки
    def __hash_fun(self, key):
        sum_value = 0
        if isinstance(key, str):
            for letter in key:
                sum_value += ord(letter)
            self.__hash_status = self.HASH_OK
        else:
            self.__hash_status = self.HASH_ERR
        return sum_value % self.__size

    def __increase_key_hash(self, index):
        index += self.__step
        if index >= self.__size:
            index -= self.__size
        return index

    def __write_into_dict(self, position, key, value):
        self.__slots[position] = key
        self.__values[position] = value

    # запросы на получение статусов выполнения public-функций
    def get_get_status(self):
        return self.__get_status

    def get_put_status(self):
        return self.__put_status

    def get_remove_status(self):
        return self.__remove_status
