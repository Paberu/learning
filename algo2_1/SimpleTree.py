class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def delete_child(self, child):
        self.Children.remove(child)
        if child.Children:
            for each_child_to_delete in child.Children:
                child.delete_child(each_child_to_delete)
        child.Parent = None
        del child

    def delete_all_children(self):
        for child in self.Children:
            self.delete_child(child)

    def get_all_descendantes(self):
        nodes = []
        if not self.Children:
            return [self]
        else:
            nodes.append(self)
            for child_node in self.Children:
                nodes.extend(child_node.get_all_descendantes())
        return nodes

    def move(self, parent):
        self.Parent.Children.remove(self)
        parent.Children.append(self)
        self.Parent = parent

    def get_descendantes_by_value(self, value):
        nodes = []
        if self.NodeValue == value:
            nodes.append(self)

        if not self.Children:
            return nodes
        else:
            for child_node in self.Children:
                nodes.extend(child_node.get_descendantes_by_value(value))
        return nodes


class SimpleTree:

    def __init__(self, root):
        self.Root = root   # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        delete_from_the_root = NodeToDelete.Parent is None
        if delete_from_the_root:   # удаляем дерево с корнем
            self.Root = SimpleTreeNode(None, None)
            self.AddChild(self.Root, NodeToDelete)   # создаём мнимый корень уровнем выше
        NodeToDelete.Parent.delete_child(NodeToDelete)
        if delete_from_the_root:
            self.Root = None

    def GetAllNodes(self):
        if not self.Root:
            return []
        return self.Root.get_all_descendantes()

    def FindNodesByValue(self, val):
        if not self.Root:
            return []
        return self.Root.get_descendantes_by_value(val)

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.move(NewParent)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        nodes = self.GetAllNodes()
        leafs = 0
        for node in nodes:
            if not node.Children:
                leafs += 1
        return leafs

