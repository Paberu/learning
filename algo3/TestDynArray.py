import unittest
from DynamicArray import DynArray


class TestDynArray(unittest.TestCase):

    def setUp(self):
        self.da1 = DynArray()
        self.da1.resize(4)
        self.da1.append(1)
        self.da1.append(2)
        self.da1.append(3)
        self.da1.append(4)

        self.da2 = DynArray()
        self.da2.resize(6)
        self.da2.append(1)
        self.da2.append(2)
        self.da2.append(3)
        self.da2.append(4)

        self.da3 = DynArray()
        self.da3.resize(8)
        self.da3.append(1)
        self.da3.append(2)
        self.da3.append(3)
        self.da3.append(4)
        self.da3.append(5)

    def test_insert1(self):
        self.da1.insert(2, 5)
        self.assertEqual(self.da1[2], 5)
        self.assertEqual(len(self.da1), 5)
        self.assertEqual(self.da1.capacity, 8)
        self.assertEqual(self.da1[4], 4)

    def test_insert2(self):
        self.da2.insert(2, 5)
        self.assertEqual(self.da2[2], 5)
        self.assertEqual(len(self.da2), 5)
        self.assertEqual(self.da2.capacity, 6)
        self.assertEqual(self.da2[4], 4)

    def test_insert3(self):
        self.da1.insert(0, 0)
        self.assertEqual(self.da1[0], 0)
        with self.assertRaises(IndexError):
            self.da2.insert(10, 10)

    def test_delete1(self):
        self.da3.delete(0)
        self.assertEqual(self.da3[0], 2)
        self.assertEqual(len(self.da3), 4)
        self.assertEqual(self.da3.capacity, 8)

        self.da3.delete(1)
        self.assertEqual(self.da3[1], 4)
        self.assertEqual(len(self.da3), 3)
        self.assertEqual(self.da3.capacity, 5)

unittest.main()
