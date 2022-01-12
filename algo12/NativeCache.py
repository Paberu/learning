class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        sum_value = 0
        for letter in key:
            sum_value += ord(letter)
        return sum_value % self.size

    def is_key(self, key):
        return self.get(key) is not None

    def put(self, key, value):
        basic_key_hash = self.hash_fun(key)
        if self.slots[basic_key_hash] in (key, None):
            self.slots[basic_key_hash] = key
            self.values[basic_key_hash] = value
            return basic_key_hash
        else:
            key_hash = self.increase_key_hash(basic_key_hash)
            while key_hash != basic_key_hash:
                if self.slots[key_hash] in (key, None):
                    self.slots[key_hash] = key
                    self.values[key_hash] = value
                    return key_hash
                else:
                    key_hash = self.increase_key_hash(key_hash)
        return -1

    def increase_key_hash(self, index):
        index += self.step
        if index >= self.size:
            index -= self.size
        return index
