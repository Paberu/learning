class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        sum_value = 0
        if isinstance(value, str):
            for letter in value:
                sum_value += ord(letter)
        return sum_value % self.size

    def seek_slot(self, value):
         basic_index = self.hash_fun(value)
         if self.slots[basic_index] is None:
             return basic_index
         else:
             index = self.increase_index(basic_index)
             while index != basic_index:
                 if self.slots[index] is None:
                     return index
                 else:
                     index = self.increase_index(index)
         return None

    def put(self, value):
         index = self.seek_slot(value)
         if index is not None:
             self.slots[index] = value
         return index

    def find(self, value):
        basic_index = self.hash_fun(value)
        if self.slots[basic_index] == value:
            return basic_index
        else:
            index = self.increase_index(basic_index)
            while index != basic_index:
                if self.slots[index] == value:
                    return index
                else:
                    index = self.increase_index(index)
        return None

    def increase_index(self, index):
        index += self.step
        if index >= self.size:
            index -= self.size
        return index
