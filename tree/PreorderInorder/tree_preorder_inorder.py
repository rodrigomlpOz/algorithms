class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_from_preorder_inorder(preorder, inorder):
    # implementation details
    map_idx = {val: idx for idx, val in enumerate(inorder)}
    idx_preorder = 0
    def recurse(start, end):
        nonlocal idx_preorder
        if start > end:
            return None
        root_val = preorder[idx_preorder]
        idx_preorder += 1
        idx_inorder = map_idx[root_val]

        root = TreeNode(root_val)
        root.left = recurse(start, idx_inorder-1)
        root.right = recurse(idx_inorder+1, end)

        return root
        
    return recurse(0, len(preorder)-1)




preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
x = binary_tree_from_preorder_inorder(preorder, inorder)
print(x)
