def diameterOfBinaryTree(root):
    diameter = 0

    def longest_path(node):
        if not node:
            return 0
        nonlocal diameter
        # recursively find the longest path in
        # both left child and right child
        left_path = longest_path(node.left)
        right_path = longest_path(node.right)

        # the convention for the diameter of a tree is often defined as the number of edges in the longest path between two nodes, not the number of nodes
        # that's why we don't add one to left_path + right_path
        diameter = max(diameter, left_path + right_path)

        # return the longest one between left_path and right_path;
        # remember to add 1 for the path connecting the node and its parent
        return max(left_path, right_path) + 1

    longest_path(root)
    return diameter