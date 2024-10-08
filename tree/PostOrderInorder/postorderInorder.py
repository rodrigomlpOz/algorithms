class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_inorder_postorder(inorder, postorder):
    map_inorder = {key: idx for idx, key in enumerate(inorder)}
    postorder_idx = len(postorder) - 1

    def construct_tree(left, right):
        nonlocal postorder_idx
        if left > right:
            return None

        root_val = postorder[postorder_idx]
        postorder_idx -= 1
        root = TreeNode(root_val)

        idx = map_inorder[root_val]

        # Construct right subtree first since we're going backward in postorder
        root.right = construct_tree(idx + 1, right)
        root.left = construct_tree(left, idx - 1)

        return root

    return construct_tree(0, len(inorder) - 1)
