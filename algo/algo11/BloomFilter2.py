class BloomFilter:

    def __init__(self, f_len, hash_code1, hash_code2):
        self.filter_len = f_len
        self.filter = 0b0
        self.hash_code1 = hash_code1
        self.hash_code2 = hash_code2

    @staticmethod
    def createBloomFilter(f_len, hash_code1, hash_code2):
        return BloomFilter(f_len, hash_code1, hash_code2)

    def get_hash(self, value, hash_code):
        code = 0
        for c in value:
            code = (code * hash_code + ord(c)) % self.filter_len
        return int(code)

    def add(self, value):
        self.filter |= 1 << self.get_hash(value, self.hash_code1)
        self.filter |= 1 << self.get_hash(value, self.hash_code2)

    def is_value(self, value):
        mask = 0b0 | (1 << self.get_hash(value, self.hash_code1)) | (1 << self.get_hash(value, self.hash_code2))
        result = mask & self.filter
        return mask == result
