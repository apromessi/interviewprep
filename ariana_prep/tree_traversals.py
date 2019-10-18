def get_node_list(root):
    parent = root
    if parent.left and parent.right:
        return get_node_list(parent.left) + get_node_list(parent.right)
    elif parent.left:
        return get_node_list(parent.left)
    elif parent.right:
        return get_node_list(parent.right)
    else:
        return [parent.info]

def levelOrder(root):
    #Write your code here
    node_list = get_node_list(root)
    for node in reversed(node_list):
        print(node)



pre-order?
def levelOrder(root):
    #Write your code here
    parent = root
    print(parent.info)
    if parent.left:
        levelOrder(parent.left)
    if parent.right:
        levelOrder(parent.right)


def levelOrder(root):
    #Write your code here
    visited = []
    to_visit = [root]
    while to_visit:
        node = to_visit[0]
        visited.append(str(node.info))
        if node.left:
            to_visit.append(node.left)
        if node.right:
            to_visit.append(node.right)
        to_visit.pop(0)

    print(' '.join(visited))
