class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.size = 0

    def MakeHeap(self, a: list, depth: int) -> None:
        self.size = 2**(depth+1) - 1
        if len(a) > self.size:
            return IndexError
        for each in a:
            self.Add(each)

    def GetMax(self):
        heap = self.HeapArray  # использование псевдонима для внутреннего массива кучи
        if len(heap) == 0:
            return -1
        elif len(heap) == 1:
            return heap.pop()
        else:
            max_to_return = heap[0]
            heap[0] = heap.pop()
            current_index = 0
            left_child_index = 2 * current_index + 1
            right_child_index = left_child_index + 1
            if left_child_index >= len(heap):
                return max_to_return
            else:
                current_index = 0
                while heap[current_index] < heap[left_child_index] or heap[current_index] < heap[left_child_index]:
                    if heap[left_child_index] > heap[right_child_index]:
                        heap[current_index], heap[left_child_index] = heap[left_child_index], heap[current_index]
                        current_index = left_child_index
                    else:
                        heap[current_index], heap[right_child_index] = heap[right_child_index], heap[current_index]
                        current_index = right_child_index
                    left_child_index = 2 * current_index + 1
                    right_child_index = left_child_index + 1
                return max_to_return

    def Add(self, key):
        heap = self.HeapArray  # использование псевдонима для внутреннего массива кучи
        if len(heap) == 0:  # добавление в пустую кучу
            heap.append(key)
        elif len(heap) == self.size:
            return False  # последняя ячейка в массиве кучи занята
        else:
            heap.append(key)
            current_index = len(heap) - 1
            parent_index = int((current_index - 1) / 2)
            while heap[current_index] > heap[parent_index]:  # подъём вверх по правой ветке
                heap[current_index], heap[parent_index] = heap[parent_index], heap[current_index]
                current_index = parent_index
                parent_index = int((current_index - 1) / 2)
            left_child_index = 2 * current_index + 1
            if left_child_index >= len(heap):
                return True
            while heap[current_index] < heap[left_child_index]:  # и спуск вниз по левой
                heap[current_index], heap[left_child_index] = heap[left_child_index], heap[current_index]
                current_index = left_child_index
                left_child_index = 2 * current_index + 1
                if left_child_index >= len(heap):
                    return True
        return True