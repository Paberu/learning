import unittest
from BloomFilter2 import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloomFilter = BloomFilter.createBloomFilter(32, 17, 223)
        self.test_strings = []
        self.test_strings.append('0123456789')
        self.test_strings.append('1234567890')
        self.test_strings.append('2345678901')
        self.test_strings.append('3456789012')
        self.test_strings.append('4567890123')
        self.test_strings.append('5678901234')
        self.test_strings.append('6789012345')
        self.test_strings.append('7890123456')
        self.test_strings.append('8901234567')
        self.test_strings.append('9012345678')

    def test_add(self):
        for test_string in self.test_strings:
            self.bloomFilter.add(test_string)
        self.assertNotEqual(self.bloomFilter.filter, 0b0)
        # print('{0:b}'.format(self.bloomFilter.filter))

    def test_is_value(self):
        for test_string in self.test_strings:
            self.bloomFilter.add(test_string)
        self.assertTrue(self.bloomFilter.is_value(self.test_strings[0]))
        self.assertTrue(self.bloomFilter.is_value(self.test_strings[4]))
        self.assertTrue(self.bloomFilter.is_value(self.test_strings[7]))
        self.assertFalse(self.bloomFilter.is_value('0192837465'))
        self.assertFalse(self.bloomFilter.is_value('5647382910'))


unittest.main()
