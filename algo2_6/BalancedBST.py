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
        sorted_array = sorted(a)
        size = len(sorted_array)
        middle = int((size - 1) / 2)
        current_node = BSTNode(sorted_array[middle], None)

        if self.Root is None:
            self.Root = current_node
        current_node.LeftChild = BSTNode(self.GenerateTree(a[]))


    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node

    def generate_subtree(self, parent, subarray):
        size = len(subarray)
        if size > 3:
            middle = int((size - 1) / 2)
            current_node = BSTNode(subarray[middle], parent)
            current_node.Level = parent.Level + 1
            current_node.LeftChild = self.generate_subtree(parent, subarray[:middle])
            current_node.RightChild = self.generate_subtree(parent, subarray[middle:])
        else:
            if size == 2:
                current_node = BSTNode(max(subarray), parent)
                current_node.Level = parent.Level + 1
                if subarray[0] < subarray[1]:
                    parent.LeftChild = current_node
                    current_node.LeftChild = self.generate_subtree(parent, [min(subarray)])
                else:
                    parent.RightChild = current_node
                    current_node.RightChild = self.generate_subtree(parent, [min(subarray)])
            else:
                current_node = BSTNode(subarray[0], parent)
                current_node.Level = parent.Level + 1
                if current_node.NodeKey < parent.NodeKey:
                    parent.LeftChild = current_node
                else:
                    parent.RightChild = current_node
                return current_node
