class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.step = 3
        while self.size % self.step == 0:
            self.step += 2
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        sum_value = 0
        for letter in key:
            sum_value += ord(letter)
        return sum_value % self.size

    def is_key(self, key):
        basic_key_hash = self.hash_fun(key)
        if self.slots[basic_key_hash] == key:
            return True
        else:
            key_hash = self.increase_key_hash(basic_key_hash)
            while key_hash != basic_key_hash:
                if self.slots[key_hash] == key:
                    return True
                else:
                    key_hash = self.increase_key_hash(key_hash)
        return False

    # def put(self, key, value):
    #     if self.is_key(key):
    #     key_hash = self.seek_slot(value)
    #     if index is not None:
    #         self.slots[index] = value
    #     return index

    def get(self, key):
        if self.is_key(key):
            key_hash =
        return None

    def increase_key_hash(self, index):
        index += self.step
        if index >= self.size:
            index -= self.size
        return index