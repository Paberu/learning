class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):

    # создаём дерево с нуля из неотсортированного массива a
    # ...

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node