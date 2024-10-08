def lowestCommonAncestor(root, p, q) -> TreeNode:
    # Iterate through the BST
    while root:
        if p.val < root.val and q.val < root.val:
            # If both nodes are smaller than the root, move to the left subtree
            root = root.left
        elif p.val > root.val and q.val > root.val:
            # If both nodes are larger than the root, move to the right subtree
            root = root.right
        else:
            # We've found the split point, so this is the LCA
            return root
