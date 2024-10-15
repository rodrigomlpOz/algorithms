class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_lca(root, p, q):
    # If we reach a leaf node or one of the target nodes, return the current node (or None)
    if root is None or root == p or root == q:
        return root

    # Recur for left and right subtrees
    left_lca = tree_lca(root.left, p, q)
    right_lca = tree_lca(root.right, p, q)

    # If both left and right subtrees return a non-None value, current node is LCA
    if left_lca and right_lca:
        return root

    # If one subtree returns None, the other subtree contains both nodes
    return left_lca if left_lca is not None else right_lca
