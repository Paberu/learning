import unittest
from NativeDictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):

    def setUp(self):
        self.dict1 = NativeDictionary(17)
        self.dict2 = NativeDictionary(21)
        self.test_string1 = '''
                    Python is an interpreted high-level general-purpose programming language.
                    Its design philosophy emphasizes code readability with its use
                     '''
        self.test_string2 = '''
                    Python is an interpreted high-level general-purpose programming language.
                    Its design philosophy emphasizes code readability with its use of significant indentation.
                    Test2
                    '''

    def test_put1(self):
        str_list = self.test_string1.split()
        for every_str in str_list:
            self.dict1.put(every_str, every_str)
            self.assertNotEqual(self.dict1.get_put_status(), NativeDictionary.PUT_ERR)

    def test_put2(self):
        str_list = self.test_string2.split()
        for every_str in str_list:
            self.dict2.put(every_str, every_str)
            self.assertNotEqual(self.dict2.get_put_status(), NativeDictionary.PUT_ERR)
        self.dict2.put('Python', 'imlovingit')
        self.assertNotEqual(self.dict2.get_put_status(), NativeDictionary.PUT_ERR)
        self.assertEqual(self.dict2.get('Python'), 'imlovingit')

    def test_get1(self):
        str_list = self.test_string1.split()
        for every_str in str_list:
            self.dict1.put(every_str, every_str)
        self.assertEqual(self.dict1.get('Python'), 'Python')
        self.assertEqual(self.dict1.get('interpreted'), 'interpreted')
        self.assertEqual(self.dict1.get('high-level'), 'high-level')
        self.assertEqual(self.dict1.get('general-purpose'), 'general-purpose')
        self.assertEqual(self.dict1.get('programming'), 'programming')
        self.assertEqual(self.dict1.get('philosophy'), 'philosophy')

    def test_get2(self):
        str_list = self.test_string2.split()
        for every_str in str_list:
            self.dict2.put(every_str, every_str)
        self.assertEqual(self.dict2.get('readability'), 'readability')
        self.assertEqual(self.dict2.get('RubyOnRails'), None)
        self.assertEqual(self.dict2.get_get_status(), NativeDictionary.GET_ERR)

    def test_is_key(self):
        str_list = self.test_string1.split()
        for every_str in str_list:
            self.dict1.put(every_str, every_str)
        self.assertTrue(self.dict1.is_key('Python'))
        self.assertTrue(self.dict1.is_key('high-level'))
        self.assertTrue(self.dict1.is_key('general-purpose'))
        self.assertFalse(self.dict1.is_key('self-taught'))
        self.assertFalse(self.dict1.is_key('self-made'))

    def test_remove(self):
        str_list = self.test_string1.split()
        for every_str in str_list:
            self.dict1.put(every_str, every_str)
        self.dict1.remove('readability')
        self.assertEqual(self.dict1.get_remove_status(), NativeDictionary.REMOVE_OK)
        self.dict1.remove('RubyOnRails')
        self.assertEqual(self.dict1.get_remove_status(), NativeDictionary.REMOVE_ERR)


unittest.main()
