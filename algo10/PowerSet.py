class PowerSet():

    def __init__(self):
        self.inner_size = 29
        self.insides = [None] * self.inner_size
        self.length = 0

    def size(self):
        return self.length

    def hash_fun(self, value):
        sum_value = 0
        if isinstance(value, str):
            for letter in value:
                sum_value += ord(letter)
        elif isinstance(value, int):
            sum_value = value
        return sum_value % self.inner_size

    def put(self, value):
        index = self.hash_fun(value)
        if self.insides[index] is None:
            self.insides[index] = [value]
            self.length += 1
        else:
            if value not in self.insides[index]:
                self.insides[index].append(value)
                self.length += 1

    def get(self, value):
        index = self.hash_fun(value)
        if self.insides[index] is not None and value in self.insides[index]:
            return True
        return False

    def remove(self, value):
        index = self.hash_fun(value)
        if self.insides[index] is not None and value in self.insides[index]:
            self.insides[index].remove(value)
            self.length -= 1
            return True
        return False

    def intersection(self, set2):
        inter_set = PowerSet()
        for each in self.insides:
            if each is not None:
                for value in each:
                    if set2.get(value):
                        inter_set.put(value)
        return inter_set

    def union(self, set2):
        union_set = self.copy()
        for each in set2.insides:
            if each is not None:
                for value in each:
                    union_set.put(value)
        return union_set

    def difference(self, set2):
        diff_set = PowerSet()
        for each in self.insides:
            if each is not None:
                for value in each:
                    if not set2.get(value):
                        diff_set.put(value)
        return diff_set

    def issubset(self, set2):
        for each in set2.insides:
            if each is not None:
                for value in each:
                    if not self.get(value):
                        return False
        return True

    def copy(self):
        copy_set = PowerSet()
        for each in self.insides:
            if each is not None:
                for value in each:
                    copy_set.put(value)
        return copy_set
