class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_inorder_postorder(inorder, postorder):
    # Build a hash map for quick index lookup in the inorder list
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    # Start from the last element of postorder (which is the root)
    post_idx = [len(postorder) - 1]  # Using a list to maintain reference
    
    # Recursive helper function
    def build_tree(in_start, in_end):
        if in_start > in_end:
            return None

        # Get the root value from postorder
        root_val = postorder[post_idx[0]]
        post_idx[0] -= 1  # Move to the next root value (going backwards)

        # Create the root node
        root = TreeNode(root_val)

        # Get the root index from the inorder map
        idx = inorder_map[root_val]

        # Recursively build right and left subtrees
        # Build right subtree first since we're processing postorder in reverse
        root.right = build_tree(idx + 1, in_end)
        root.left = build_tree(in_start, idx - 1)

        return root
    
    # Build the tree with full range of inorder indices
    return build_tree(0, len(inorder) - 1)

# Example test case
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = construct_binary_tree_from_inorder_postorder(inorder, postorder)
