import ctypes


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
    DELETE_NIL: Final = 0
    DELETE_OK: Final = 1
    DELETE_ERR: Final = 2

    def __init__(self, capacity = 16):
        self._count = 0
        self._capacity = capacity
        self._array = self.make_array(self.capacity)

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

    # постусловие:
    @staticmethod
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __len__(self):
        return self._count

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            self._get_status = self.GET_ERR
            return 0
        self._get_status = self.GET_OK
        return self.array[i]

    def resize(self, new_capacity):
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

    def append(self, item):
        if self._count >= self._capacity:
            self._append_status = self.APPEND_ERR
        else:
            self._array[self._count] = item
            self._count += 1
            self._append_status = self.APPEND_OK

    def insert(self, i, item):
        if i < 0 or i > self.count:
            self._insert_status = self.INSERT_ERR
        elif i == self.count:
            self.append(item)
        else:
            if self.count == self.capacity:
                self._insert_status = self.INSERT_ERR
            else:
                # расписать insert
            self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        else:
            if self.capacity == 16 or self.count - 1 >= self.capacity / 2:
                for j in range(i, self.count-1):
                    self.array[j] = self.array[j+1]
                self.array[self.count-1] = ctypes.py_object
            else:
                if self.capacity/1.5 < 16:
                    self.capacity = 16
                else:
                    self.capacity = int(self.capacity/1.5)
                new_array = self.make_array(self.capacity)
                if i > 0:
                    for j in range(i):
                        new_array[j] = self.array[j]
                for j in range(i+1, self.count):
                    new_array[j-1] = self.array[j]
                self.array = new_array
            self.count -= 1
