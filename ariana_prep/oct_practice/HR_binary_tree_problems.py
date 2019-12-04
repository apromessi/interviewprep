'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
'''

# The height of a binary tree is the number of edges between the
# tree's root and its furthest leaf.

def height(root):
    if root.left and root.right:
        return 1 + max(height(root.left), height(root.right))
    elif root.left:
        return 1 + height(root.left)
    elif root.right:
        return 1 + height(root.right)
    else:
        return 0


# Find lowest common ancestor of two node values in a binary search tree

def lca(root, v1, v2):
    current = root
    while current.info != v1 and current.info != v2:
        if current.left and v1 < current.info and v2 < current.info:
            current = current.left
        elif current.right and v1 > current.info and v2 > current.info:
            current = current.right
        else:
            return current

    return current
