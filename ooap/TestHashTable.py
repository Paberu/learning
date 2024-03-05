import unittest


from HashTable import HashTable


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(10)

    def test_hash_fun(self):
        self.assertEqual(self.hash_table.hash_fun('test_of_hash_table'), 6)
        self.assertEqual(self.hash_table.hash_fun('second_test_of_hash_table'), 7)

    def test_seek_slot(self):
        self.assertEqual(self.hash_table.seek_slot('test_of_hash_table'), 6)
        self.assertEqual(self.hash_table.seek_slot('second_test_of_hash_table'), 7)

    def test_put(self):
        self.hash_table.put('test_of_hash_table')
        self.assertEqual(self.hash_table.get_put_status(), HashTable.PUT_OK)
        self.hash_table.put('second_test_of_hash_table')
        self.assertEqual(self.hash_table.get_put_status(), HashTable.PUT_OK)

    def test_find(self):
        self.hash_table.put('test_of_hash_table')
        self.hash_table.put('second_test_of_hash_table')
        self.assertEqual(self.hash_table.find('test_of_hash_table'), 6)
        self.assertEqual(self.hash_table.get_find_status(), HashTable.FIND_OK)
        self.assertEqual(self.hash_table.find('second_test_of_hash_table'), 7)
        self.assertEqual(self.hash_table.get_find_status(), HashTable.FIND_OK)
        self.hash_table.find('not_in_there')
        self.assertEqual(self.hash_table.get_find_status(), HashTable.FIND_ERR)


unittest.main()
