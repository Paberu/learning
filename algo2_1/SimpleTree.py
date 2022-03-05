class SimpleTreeNode:

    def __init__(self, val=None, parent=None):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        if parent:
            self.set_parent(parent)

    def set_parent(self, parent):
        self.Parent = parent
        parent.Children.append(self)

    def delete_child(self, child):
        self.Children.remove(child)
        if child.Children:
            for each_child_to_delete in child.Children:
                child.delete_child(each_child_to_delete)
        child.Parent = None
        del child

    def delete_all_children(self):
        self.Children.clear()

    def get_all_Descendantes(self):
        nodes = []
        if not self.Children:
            return [self]
        else:
            nodes.append(self)
            for child_node in self.Children:
                nodes.extend(child_node.get_all_Descendantes())
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

    def __init__(self, root=None):
        self.Root = root   # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        NewChild.set_parent(ParentNode)

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
        return self.Root.get_all_Descendantes()

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

