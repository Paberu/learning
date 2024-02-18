import unittest
from NativeCache import NativeCache


class TestNativeCache(unittest.TestCase):

    def setUp(self):
        self.cache1 = NativeCache(12)
        self.cache2 = NativeCache(10)
        self.test_string = '''
                    Python is an interpreted high-level general-purpose programming language.
                    Its design philosophy emphasizes code readability with its use of significant indentation.
                    Test2
                    '''

    def test_put_str(self):
        test_strings = self.test_string.split()
        for i in range(len(test_strings)):
            self.cache1.put(test_strings[i], test_strings[i])
        self.assertEqual(self.cache1.get('Test2'), 'Test2')
        self.assertEqual(self.cache1.get('indentation.'), 'indentation.')
        self.assertEqual(self.cache1.get('readability.'), None)

    def test_put_num(self):
        for i in range(10):
            self.cache2.put(i, i)
        self.cache2.put(12, 12)
        self.assertEqual(self.cache2.get(12), 12)
        self.assertEqual(self.cache2.get(2), None)

    def test_complicated_get(self):
        test_strings = self.test_string.split()
        for i in range(12):
            self.cache1.put(test_strings[i], test_strings[i])
        for i in range(11, 0, -1):
            for j in range(i, 0, -1):
                self.cache1.get(test_strings[j])
        for i in range(12, len(test_strings)):
            self.cache1.put(test_strings[i], test_strings[i])
            self.assertEqual(self.cache1.slots[6], test_strings[i])


unittest.main()
