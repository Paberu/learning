import unittest
from HashTable import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash1 = HashTable(17, 3)
        self.test_string = '''
            Python is an interpreted high-level general-purpose programming language.
            Its design philosophy emphasizes code readability with its use of significant indentation.
            Its language constructs as well as its object-oriented approach aim to help programmers
            write clear, logical code for small and large-scale projects.

            Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms,
            including structured (particularly, procedural), object-oriented and functional programming.
            It is often described as a "batteries included" language due to its comprehensive standard library.
            '''
        self.hash2 = HashTable(17, 3)
        str_list = self.test_string.split()
        for every_str in str_list:
            slot = self.hash2.put(every_str)
            if slot is None:
                break

    def test_hash_fun(self):
        str_list = self.test_string.split()
        for every_str in str_list:
            self.assertEqual(self.hash1.hash_fun('Python'), 13)
            self.assertEqual(self.hash1.hash_fun('is'), 16)
            self.assertEqual(self.hash1.hash_fun('an'), 3)
            self.assertEqual(self.hash1.hash_fun('interpreted'), 0)
            self.assertEqual(self.hash1.hash_fun('high-level'), 11)
            self.assertEqual(self.hash1.hash_fun('general-purpose'), 14)
            self.assertEqual(self.hash1.hash_fun('programming'), 14)
            self.assertEqual(self.hash1.hash_fun('language.'), 15)
            self.assertEqual(self.hash1.hash_fun('Its'), 15)
            self.assertEqual(self.hash1.hash_fun('design'), 5)
            self.assertEqual(self.hash1.hash_fun('philosophy'), 15)
            self.assertEqual(self.hash1.hash_fun('emphasizes'), 10)
            self.assertEqual(self.hash1.hash_fun('code'), 3)
            self.assertEqual(self.hash1.hash_fun('readability'), 6)
            self.assertEqual(self.hash1.hash_fun('with'), 2)
            self.assertEqual(self.hash1.hash_fun('its'), 13)
            self.assertEqual(self.hash1.hash_fun('use'), 10)

    def test_seek_slot(self):
        str_list = self.test_string.split()
        for i in range(6):
            self.hash1.put(str_list[i])
        self.assertEqual(self.hash1.seek_slot('programming'), 6)
        self.assertEqual(self.hash1.seek_slot('language.'), 15)
        self.assertEqual(self.hash1.seek_slot('code'), 6)

    def test_put(self):
        self.assertEqual(self.hash1.put('Python'), 13)
        self.assertEqual(self.hash1.put('is'), 16)
        self.assertEqual(self.hash1.put('an'), 3)
        self.assertEqual(self.hash1.put('interpreted'), 0)
        self.assertEqual(self.hash1.put('high-level'), 11)
        self.assertEqual(self.hash1.put('general-purpose'), 14)
        self.assertEqual(self.hash1.put('programming'), 6)
        self.assertEqual(self.hash1.put('language.'), 15)
        self.assertEqual(self.hash1.put('Its'), 1)
        self.assertEqual(self.hash1.put('design'), 5)
        self.assertEqual(self.hash1.put('philosophy'), 4)
        self.assertEqual(self.hash1.put('emphasizes'), 10)

    def test_find(self):
        self.assertEqual(self.hash2.find('readability'), 12)
        self.assertEqual(self.hash2.find('programming'), 6)
        self.assertEqual(self.hash2.find('language.'), 15)
        self.assertEqual(self.hash2.find('interpreted'), 0)
        self.assertEqual(self.hash2.find('Python'), 13)
        self.assertEqual(self.hash2.find('code'), 9)

unittest.main()
