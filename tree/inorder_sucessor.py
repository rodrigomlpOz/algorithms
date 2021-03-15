#9.10
def find_successor(node):

    if node.right:
        # Successor is the leftmost element in node's right subtree.
        node = node.right
        while node.left:
            node = node.left
        return node

    # Find the closest ancestor whose left subtree contains node.
    while node.parent and node.parent.right is node:
        node = node.parent

    # A return value of None means node does not have successor, i.e., node is
    # the rightmost node in the tree.
    return node.parent
