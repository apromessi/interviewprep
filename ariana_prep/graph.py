#!/usr/bin/env python


class Node(object):
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors else []

    def __repr__(self):
        return 'value: {}'.format(self.value)


class Graph(object):
    def __init__(self, nodes=None):
        self.nodes = nodes if nodes else []

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
            return True
        else:
            return False

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.neighbors.remove(node2)
            node2.neighbors.remove(node1)
            return True
        else:
            return False


def main():
    graph = Graph()
    node1 = Node(1)
    node2 = Node(2)
    graph.nodes = [node1, node2]

    graph.add_edge(node1, node2)

    print(node1.neighbors)
    print(node2.neighbors)

    graph.remove_edge(node1, node2)

    print(node1.neighbors)
    print(node2.neighbors)

if __name__ == '__main__':
    main()
