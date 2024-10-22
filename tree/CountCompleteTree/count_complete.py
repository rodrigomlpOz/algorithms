def countNodes(root) -> int:
    # Helper function to compute the depth of the tree
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.left  # Traverse down the leftmost path
        return depth
    if not root:
        return 0

    # Get the depth of the left and right subtrees
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)

    if left_depth == right_depth:
        # Left subtree is a perfect binary tree
        # Number of nodes in left subtree is 2^left_depth - 1, plus the root node (+1)
        return (2 ** left_depth - 1) + 1 + countNodes(root.right)
    else:
        # Right subtree is a perfect binary tree
        # Number of nodes in right subtree is 2^right_depth - 1, plus the root node (+1)
        return (2 ** right_depth - 1) + 1 + countNodes(root.left)
