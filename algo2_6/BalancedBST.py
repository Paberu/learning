class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла

        if parent is not None:
            if key < parent.NodeKey:
                parent.LeftChild = self
            else:
                parent.RightChild = self
            self.Level = parent.Level + 1

    def find_leaves(self):
        leaves = []
        if self.LeftChild is None and self.RightChild is None:
            return [self]
        else:
            if self.LeftChild is not None:
                leaves.extend(self.LeftChild.find_leaves())
            if self.RightChild is not None:
                leaves.extend(self.RightChild.find_leaves())
        return leaves


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        sorted_array = sorted(a)
        size = len(sorted_array)
        middle = int((size - 1) / 2)
        self.Root = BSTNode(sorted_array[middle], None)
        if size > 2:
            self.Root.LeftChild = self.generate_subtree(self.Root, sorted_array[:middle])
            self.Root.RightChild = self.generate_subtree(self.Root, sorted_array[middle+1:])
        elif size == 2:
            self.Root.RightChild = self.generate_subtree(self.Root, sorted_array[middle + 1:])
        else:
            pass  # нечего добавить, что делать, если else не нужен

    def generate_subtree(self, parent, subarray):
        size = len(subarray)
        if size > 2:
            middle = int((size - 1) / 2)
            current_node = BSTNode(subarray[middle], parent)
            current_node.LeftChild = self.generate_subtree(current_node, subarray[:middle])
            current_node.RightChild = self.generate_subtree(current_node, subarray[middle+1:])
        else:
            if size == 2:
                if max(subarray) < parent.NodeKey:
                    current_node = BSTNode(max(subarray), parent)
                    current_node.LeftChild = BSTNode(min(subarray), current_node)
                else:
                    current_node = BSTNode(min(subarray), parent)
                    current_node.RightChild = BSTNode(max(subarray), current_node)
            else:
                current_node = BSTNode(subarray[0], parent)
        return current_node

    def IsBalanced(self, root_node):
        leaves = root_node.find_leaves()
        leaf_levels = []
        for leaf in leaves:
            leaf_levels.append(leaf.Level)
        if max(leaf_levels) - min(leaf_levels) > 1:
            return False
        else:
            return True