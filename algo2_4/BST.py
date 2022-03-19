class aBST:

    def __init__(self, depth):
        tree_size = 2**(depth+1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        index = 0
        tree_size = len(self.Tree)
        while self.Tree[index] is not None and index < tree_size:
            if self.Tree[index] > key:
                index = 2*index + 1
            elif self.Tree[index] < key:
                index = 2*index + 2
            else:  # == key
                return index
        if self.Tree[index] is None:
            return -index
        return None  # не найден

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index < 0:
            self.Tree[-index] = key
            return -index
        elif index > 0:
            return index
        else:
            if not self.Tree[0]:
                self.Tree[0] = key
                return 0
            else:
                return -1
