class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


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
        node = self.Root ### что делать, если дерево пустое???
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
        # ищем в дереве узел и сопутствующую информацию по ключу
        return None  # возвращает BSTFind

    def AddKeyValue(self, key, val):
        node = self.Root
        while node:
            if key < node.NodeKey:
                if not node.LeftChild:
                    node.LeftChild = BSTNode(key, val, node)
                    return True
                else:
                    node = node.LeftChild
            elif key > node.NodeKey:
                if not node.RightChild:
                    node.RightChild = BSTNode(key, val, node)
                    return True
                else:
                    node = node.RightChild
            else:
                return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве
