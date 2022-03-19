class aBST:

    def __init__(self, depth):
        tree_size = 2**(depth+1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        index = 0
        tree_size = len(self.Tree)
        while index < tree_size and self.Tree[index] is not None:
            if self.Tree[index] > key:
                index = 2*index + 1
            elif self.Tree[index] < key:
                index = 2*index + 2
            else:  # == key
                return index
        if index > tree_size:
            return None
        else:  # self.Tree[index] is not None
            return -index

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1

        if index < 0:
            self.Tree[-index] = key
            return -index
        elif index > 0:
            return index
        else:  # index == 0
            if self.Tree[0] == key:  # Tree[0] has a key
                return 0
            elif not self.Tree[0]:  # Tree == [None] * depth
                self.Tree[0] = key
                return 0
