class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        for node in NodeToDelete.Children:
            self.DeleteNode(node)
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        del NodeToDelete

    def GetAllNodes(self):
        nodes = []
        nodes.extend(self.getAllDescendantes(self.Root))
        return nodes

    def getAllDescendantes(self, node):
        nodes = []
        if not node.Children:
            return [node]
        else:
            nodes.append(node)
            for child_node in node.Children:
                if not child_node.Children:
                    nodes.append(child_node)
                else:
                    nodes.extend(self.getAllDescendantes(child_node))
        return nodes


    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        return []

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        # количество листьев в дереве
        return 0