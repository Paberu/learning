class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0b0

    def hash1(self, str1):
        # 17
        code = 0
        for c in str1:
            code = (code * 17 + ord(c)) % self.filter_len
        return int(code)

    def hash2(self, str1):
        # 223
        code = 0
        for c in str1:
            code = (code * 223 + ord(c)) % self.filter_len
        return int(code)

    def add(self, str1):
        position1 = self.hash1(str1)
        position2 = self.hash2(str1)
        self.filter |= 1 << position1
        self.filter |= 1 << position2

    def is_value(self, str1):
        position1 = self.hash1(str1)
        position2 = self.hash2(str1)
        mask = 0b0 | (1 << position1) | (1 << position2)
        result = mask & self.filter
        return mask == result
