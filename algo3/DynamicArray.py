import ctypes


class DynArray:

    def __init__(self, capacity = 16):
        self.count = 0
        self.capacity = capacity
        self.array = self.make_array(self.capacity)

    @staticmethod
    def create_dynamic_array(capacity):
        dyn_array = DynArray(capacity)
        return dyn_array

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        if new_capacity < 16:
            new_capacity = 16
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count:
            self.append(itm)
        else:
            if self.count == self.capacity:
                self.capacity *= 2
                new_array = self.make_array(self.capacity)
                for j in range(i):
                    new_array[j] = self.array[j]
                new_array[i] = itm
                for j in range(i, self.count):
                    new_array[j+1] = self.array[j]
                self.array = new_array
            else:
                for j in range(self.count, i, -1):
                    self.array[j] = self.array[j-1]
                self.array[i] = itm
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
