import unittest
from BSR_func import GenerateBBSTArray


class TestSimpleTree(unittest.TestCase):
    def test_func(self):
        array = [x for x in range(1, 6)]
        self.assertEqual(GenerateBBSTArray(array), [3,2,4,1,5])


unittest.main()
