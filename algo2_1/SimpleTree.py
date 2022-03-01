class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        
    def add_child(self, child):
        self.Children.append(child)
        child.set_parent(self)

    def set_parent(self, parent):
        self.Parent = parent

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



class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    # def AddChild(self, ParentNode, NewChild):
    #     NewChild.Parent = ParentNode
    #     ParentNode.Children.append(NewChild)

    def AddChild(self, ParentNode, NewChild):
        ParentNode.add_child(NewChild)

    # def DeleteNode(self, NodeToDelete):
    #     for node in NodeToDelete.Children:
    #         self.DeleteNode(node)
    #     NodeToDelete.Parent.Children.remove(NodeToDelete)
    #     del NodeToDelete

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is None: # удаляем дерево с корнем
            new_root = SimpleTreeNode(None, None)
            self.AddChild(new_root, NodeToDelete) # создаём мнимый корень уровнем выше
            self.Root = new_root
        NodeToDelete.Parent.delete_child(NodeToDelete)

    def GetAllNodes(self):
        return self.Root.get_all_Descendantes()

    # def getAllDescendantes(self, node):
    #     nodes = []
    #     if not node.Children:
    #         return [node]
    #     else:
    #         nodes.append(node)
    #         for child_node in node.Children:
    #             if not child_node.Children:
    #                 nodes.append(child_node)
    #             else:
    #                 nodes.extend(self.getAllDescendantes(child_node))
    #     return nodes


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