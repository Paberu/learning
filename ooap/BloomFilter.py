from importlib.metadata import FileHash
from typing import Final


class BloomFilter:

    HASH_NIL: Final = 0
    HASH_OK: Final = 1
    HASH_ERR: Final = 2

    # конструктор
    def __init__(self, f_len, hash_code1, hash_code2):
        self._filter_len = f_len
        self._filter = 0b0
        self._hash_code1 = hash_code1
        self._hash_code2 = hash_code2

        self._hash_status = self.HASH_NIL

    # запросы
    # предусловие: передаётся строковое значение и числовой хэш-код
    # постусловие: возвращает номер бита, в котором устанавливается 1
    def _get_hash(self, value, hash_code):
        code = 0
        if isinstance(value, str) and isinstance(hash_code, int):
            for c in value:
                code = (code * hash_code + ord(c)) % self._filter_len
            self._hash_status = self.HASH_OK
        else:
            self._hash_status = self.HASH_ERR
        return int(code)

    # постусловие: возвращает результат проверки
    def is_value(self, value):
        if not isinstance(value, str):
            value = str(value)
        mask = 0b0 | (1 << self._get_hash(value, self._hash_code1)) | (1 << self._get_hash(value, self._hash_code2))
        result = mask & self._filter
        return mask == result

    # команды
    # постусловие: строка (или строковое выражение объекта) зафиксированы в теле фильтра
    def add(self, value):
        if not isinstance(value, str):
            value = str(value)
        self._filter |= 1 << self._get_hash(value, self._hash_code1)
        self._filter |= 1 << self._get_hash(value, self._hash_code2)

    # запросы статусов выполнения команд
    def get_hash_status(self):
        return self._hash_status
