class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.step = 3
        while self.size % self.step == 0:
            self.step += 2
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
        if self.slots[basic_key_hash] is not None:
            key_hash = self.increase_key_hash(basic_key_hash)
            key_min_hit = basic_key_hash if self.hits[basic_key_hash] < self.hits[key_hash] else key_hash
            while key_hash != basic_key_hash:
                if self.slots[key_hash] is not None:
                    key_hash = self.increase_key_hash(key_hash)
                    key_min_hit = key_hash if self.hits[key_hash] < self.hits[key_min_hit] else key_min_hit
                else:
                    self.set(key_hash, key, value)
                    return key_hash
            self.set(key_min_hit, key, value)
            return key_min_hit
        self.set(basic_key_hash, key, value)
        return basic_key_hash

    def get(self, key):
        basic_key_hash = self.hash_fun(key)
        if self.slots[basic_key_hash] == key:
            return self.values[basic_key_hash]
        else:
            key_hash = self.increase_key_hash(basic_key_hash)
            while key_hash != basic_key_hash:
                if self.slots[key_hash] == key:
                    return self.values[key_hash]
                else:
                    key_hash = self.increase_key_hash(key_hash)
        return None

    def increase_key_hash(self, index):
        index += self.step
        if index >= self.size:
            index -= self.size
        return index

    def set(self, key_hash, key, value):
        self.slots[key_hash] = key
        self.values[key_hash] = value
        self.hits[key_hash] = 0