import unittest
from BSR_func import GenerateBBSTArray


class TestSimpleTree(unittest.TestCase):

    def test_func(self):
        array = [x for x in range(1, 8)]
        self.assertEqual(GenerateBBSTArray(array), [4, 2, 6, 1, 3, 5, 7])

    def test_func2(self):
        array = [x for x in range(1, 4)]
        self.assertEqual(GenerateBBSTArray(array), [2, 1, 3])

    def test_func3(self):
        array = [1]
        self.assertEqual(GenerateBBSTArray(array), [1])


unittest.main()
