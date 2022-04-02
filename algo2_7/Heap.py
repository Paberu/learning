from pip._internal.cli.cmdoptions import hash


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
        elif len(heap) in (1, 2):
            return heap.pop(0)
        else:
            max_to_return = heap[0]
            heap[0] = heap.pop()
            current_index = 0
            left_child_index = 2 * current_index + 1
            right_child_index = left_child_index + 1
            has_left_child = left_child_index < len(heap)
            has_right_child = right_child_index < len(heap)
            if not has_left_child:  # следовательно, и правого нет
                return max_to_return
            else:
                while has_left_child:  # иммет смысл продолжать, пока хотя бы левый сущетствует
                    child_index_for_replace = left_child_index
                    if has_right_child and heap[right_child_index] > heap[left_child_index]:
                        child_index_for_replace = right_child_index

                    if heap[child_index_for_replace] > heap[current_index]:
                        heap[current_index], heap[child_index_for_replace] = heap[child_index_for_replace], heap[current_index]
                        current_index = child_index_for_replace
                    else:
                        return max_to_return
                    left_child_index = 2 * current_index + 1
                    right_child_index = left_child_index + 1
                    has_left_child = left_child_index < len(heap)
                    has_right_child = right_child_index < len(heap)
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