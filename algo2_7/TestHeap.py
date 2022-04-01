import unittest
from Heap import Heap


class TestHeap(unittest.TestCase):

    def test_add1(self):
        heap1 = Heap()
        heap1.Add(9)
        self.assertEqual(heap1.HeapArray, [9])
        heap1.Add(7)
        self.assertEqual(heap1.HeapArray, [9, 7])
        heap1.Add(17)
        self.assertEqual(heap1.HeapArray, [17, 7, 9])
        heap1.Add(11)
        self.assertEqual(heap1.HeapArray, [17, 11, 9, 7])

    def test_make_heap(self):
        heap = Heap()
        heap.MakeHeap([4, 7, 2, 5, 1, 3, 6], 2)
        self.assertEqual(heap.HeapArray, [7, 5, 6, 4, 1, 2, 3])

    def test_get_max(self):
        heap = Heap()
        heap.MakeHeap([4, 7, 2, 5, 1, 3, 6], 2)
        self.assertEqual(heap.GetMax(), 7)
        self.assertEqual(heap.HeapArray, [6, 5, 3, 4, 1, 2])

    def test_get_max2(self):
        heap = Heap()
        heap.MakeHeap([4, 7], 1)
        self.assertEqual(heap.GetMax(), 7)
        self.assertEqual(heap.HeapArray, [4])

    def test_get_max3(self):
        heap = Heap()
        heap.MakeHeap([4], 3)
        self.assertEqual(heap.GetMax(), 4)
        self.assertEqual(heap.HeapArray, [])

unittest.main()