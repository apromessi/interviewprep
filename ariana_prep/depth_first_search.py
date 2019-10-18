#!/usr/bin/env python


from graph import Graph, Node


def depth_first_search(value, starting_node):
    pass


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
