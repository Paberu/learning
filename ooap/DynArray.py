import ctypes
from typing import Final


class DynArray:

    RESIZE_NIL: Final= 0
    RESIZE_OK: Final = 1
    RESIZE_NOT: Final = 2
    GET_NIL: Final = 0
    GET_OK: Final = 1
    GET_ERR: Final = 2
    APPEND_NIL: Final = 0
    APPEND_OK: Final = 1
    APPEND_ERR: Final = 2
    INSERT_NIL: Final = 0
    INSERT_OK: Final = 1
    INSERT_ERR: Final = 2
    INSERT_INDEX_ERROR: Final = 3
    DELETE_NIL: Final = 0
    DELETE_OK: Final = 1
    DELETE_INDEX_ERR: Final = 2

    def __init__(self, capacity = 16):
        self._count = 0
        self._capacity = capacity
        self._array = self.make_array(self._capacity)

        self._get_status = self.GET_NIL
        self._resize_status = self.RESIZE_NIL
        self._append_status = self.APPEND_NIL
        self._insert_status = self.INSERT_NIL
        self._delete_status = self.DELETE_NIL

    # постусловие: создаётся новый динамический массив
    @staticmethod
    def create_dynamic_array(capacity):
        dyn_array = DynArray(capacity)
        return dyn_array

    # постусловие: выделение памяти под динамический массив
    @staticmethod
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    # запросы
    # постусловие: возвращает счётчик массива
    def __len__(self):
        return self._count

    # постусловие: возвращает необходимое значение или 0; что получилось, смотрим по статусу
    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            self.set_get_status(self.GET_ERR)
            return 0
        self.set_get_status(self.GET_OK)
        return self.array[i]

    # команды
    # постусловие: изменение ёмкости и статуса; или бездействие в случае чрезмерного занижения ёмкости
    def _resize(self, new_capacity):
        if new_capacity < 16:
            new_capacity = 16
        if new_capacity != self._capacity:
            new_array = self.make_array(new_capacity)
            for i in range(self.count):
                new_array[i] = self.array[i]
            self._array = new_array
            self._capacity = new_capacity
            self._resize_status = self.RESIZE_OK
        else:
            self._resize_status = self.RESIZE_NOT

    # постусловие: добавить элемент в массив, если есть место; результат см. в статусе
    def _append(self, item):
        if self._count >= self._capacity:
            self.set_append_status(self.APPEND_ERR)
        else:
            self._array[self._count] = item
            self._count += 1
            self._append_status = self.APPEND_OK

    # постусловие: добавление элемента в указанное место или отказ, в случае превышения ёмкости или ошибки в индексе
    def _insert(self, i, item):
        if i < 0 or i > self.count:
            self._insert_status = self.INSERT_INDEX_ERR
        elif i == self.count:
            self._append(item)
        else:
            if self.count == self.capacity:
                self._insert_status = self.INSERT_ERR
            else:
                for j in range(self._count, i, -1):
                    self._array[j] = self._array[j - 1]
                self._array[i] = item
            self._count += 1
            self._insert_status = self.INSERT_OK

    # постусловие: удаление элемента по указанному индексу
    def _delete(self, i):
        if i < 0 or i >= self.count:
            self._delete_status = self.DELETE_INDEX_ERR
        else:
            for j in range(i, self._count-1):
                self._array[j] = self._array[j+1]
            self.count -= 1
            self._delete_status = self.DELETE_OK

    # запросы геттеры:
    def get_count(self):
        return self._count

    def get_capacity(self):
        return self._capacity

    def get_array(self):
        return self._array

    def get_get_status(self):
        return self._get_status

    def get_resize_status(self):
        return self._resize_status

    def get_append_status(self):
        return self._append_status

    def get_insert_status(self):
        return self._insert_status

    def get_delete_status(self):
        return self._delete_status
