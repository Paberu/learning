class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def count_children(self):
        count = 1  # сам себе уже есть
        if not self.LeftChild and not self.RightChild:
            return count
        else:
            if self.LeftChild:
                count += self.LeftChild.count_children()
            if self.RightChild:
                count += self.RightChild.count_children()
        return count


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        node = self.Root
        find_result = BSTFind()
        while node:
            if key == node.NodeKey:
                find_result.Node = node
                find_result.NodeHasKey = True
                return find_result
            elif key < node.NodeKey:
                if not node.LeftChild:
                    find_result.Node = node
                    find_result.NodeHasKey = False
                    find_result.ToLeft = True
                    return find_result
                else:
                    node = node.LeftChild
            else:  # key > node.NodeKey
                if not node.RightChild:
                    find_result.Node = node
                    find_result.NodeHasKey = False
                    find_result.ToLeft = False
                    return find_result
                else:
                    node = node.RightChild
        return None

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if not find_result:
            self.Root = BSTNode(key, val, None)
            return True
        if find_result.NodeHasKey:
            return False
        else:
            if find_result.ToLeft:
                find_result.Node.LeftChild = BSTNode(key, val, find_result.Node)
                return True
            else:
                find_result.Node.RightChild = BSTNode(key, val, find_result.Node)
                return True

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if not FindMax:
            while node.LeftChild:
                node = node.LeftChild
        else:
            while node.RightChild:
                node = node.RightChild
        return node

    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if not find_result or not find_result.NodeHasKey:
            return False
        else:
            node = find_result.Node
            if not node.RightChild:
                replacement_node = node.LeftChild
                parent = node.Parent
                replacement_node.Parent = parent
                parent.LeftChild = replacement_node
            else:
                replacement_node = node.RightChild
                while replacement_node.LeftChild:
                    replacement_node = replacement_node.LeftChild
                parent = node.Parent
                replacement_node.Parent.LeftChild = None
                replacement_node.Parent = parent
                parent.LeftChild = replacement_node
                replacement_node.LefChild = node.LeftChild
                replacement_node.RightChild = node.RightChild
        del node
        return True

    def Count(self):
        if not self.Root:
            return 0  # количество узлов в дереве
        else:
            return self.Root.count_children()
