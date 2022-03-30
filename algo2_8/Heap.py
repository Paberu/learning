class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.size = 0

    def MakeHeap(self, a: list, depth: int) -> None:
        self.size = 2**(depth+1) - 1
        if len(a) > self.size:
            return IndexError
        self.HeapArray[0] = a.pop(max(a))
        self.HeapArray.extend(a)

    def GetMax(self):
        max_to_return = self.HeapArray[0]
        self.HeapArray.insert(0, self.HeapArray.pop())

        # вернуть значение корня и перестроить кучу
        return -1  # если куча пуста

    def Add(self, key):
        if self.HeapArray[self.size]:
            return False
        else:
            self.HeapArray[self.size] = key
            self.size += 1
            if self.size == 1:
                return True  # добавили элемент в пустую кучу
            else:
                new_element_key = self.size - 1
                parent = int((new_element_key - 1) / 2)
                while not self.HeapArray[new_element_key] < self.HeapArray[parent]:
                    self.HeapArray[new_element_key], self.HeapArray[parent] = \
                        self.HeapArray[parent], self.HeapArray[new_element_key]
                    parent = int((new_element_key - 1) / 2)
                left_child_key = 2 * new_element_key + 1
                right_child_key = 2 * new_element_key + 2
                while not (self.HeapArray[new_element_key] > self.HeapArray[left_child_key] and
                           self.HeapArray[new_element_key] > self.HeapArray[right_child_key]):
                    if self.HeapArray[new_element_key] < self.HeapArray[left_child_key]:
                        self.HeapArray[new_element_key], self.HeapArray[left_child_key] =\
                            self.HeapArray[left_child_key], self.HeapArray[new_element_key]
                        new_element_key = 2 * new_element_key + 1
                    else:
                        self.HeapArray[new_element_key], self.HeapArray[right_child_key] =\
                            self.HeapArray[right_child_key], self.HeapArray[new_element_key]
                        new_element_key = 2 * new_element_key + 2
                return True
