#!/usr/bin/env python


class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


class Tree(object):
    def __init__(self, root):
        self.root = root

    def level_order_print(self):
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            print node.value
            if node.children:
                nodes.extend(node.children)

    def preorder_print(self, node=None):
        if not node:
            node = self.root

        print node.value

        if node.children:
            for child in node.children:
                self.preorder_print(node=child)


    def postorder_print(self, node=None):
        if not node:
            node = self.root

        if node.children:
            for child in node.children:
                self.postorder_print(node=child)

        print node.value



if __name__ == '__main__':
    root = Node(1)
    tree = Tree(root)

    children_of_root = [Node(x) for x in [2, 3, 4]]
    root.children = children_of_root

    children_of_2 = [Node(x) for x in [5, 6]]
    children_of_root[0].children = children_of_2
    children_of_3 = [Node(x) for x in [7]]
    children_of_root[1].children = children_of_3
    children_of_4 = [Node(x) for x in [8, 9]]
    children_of_root[2].children = children_of_4

    children_of_5 = [Node(x) for x in [10, 11]]
    children_of_2[0].children = children_of_5
    children_of_10 = [Node(x) for x in [12]]
    children_of_5[0].children = children_of_10

    tree.level_order_print()
    print 'expected result: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12'

    tree.preorder_print()
    print 'expected result: 1, 2, 5, 10, 12, 11, 6, 3, 7, 4, 8, 9'

    tree.postorder_print()
    print 'expected result: 12, 10, 11, 5, 6, 2, 7, 3, 8, 9, 4, 1'