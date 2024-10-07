class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_from_preorder_inorder(preorder, inorder):
    # Create an iterator for the preorder list
    preorder_iter = iter(preorder)
    
    # Helper function to build the tree recursively
    def build_tree(inorder):
        if not inorder:
            return None
        
        # Get the next root value from the preorder iterator
        root_val = next(preorder_iter)
        node = Node(root_val)
        
        # Find the index of the root in inorder list
        idx = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        node.left = build_tree(inorder[:idx])
        node.right = build_tree(inorder[idx+1:])
        
        return node

    # Start building the tree
    return build_tree(inorder)

# Example test case
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = binary_tree_from_preorder_inorder(preorder, inorder)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_from_preorder_inorder(preorder, inorder):
    # Create a map to store the index of each element in inorder for quick lookup
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    # Create an iterator for the preorder list
    preorder_iter = iter(preorder)

    # Helper function to build the tree recursively
    def build_tree(in_start, in_end):
        if in_start > in_end:
            return None

        # Get the next root value from the preorder iterator
        root_val = next(preorder_iter)
        node = Node(root_val)

        # Get the root index in inorder list using the map
        idx = inorder_map[root_val]

        # Recursively build the left and right subtrees
        node.left = build_tree(in_start, idx - 1)
        node.right = build_tree(idx + 1, in_end)

        return node

    # Start building the tree using the full range of inorder
    return build_tree(0, len(inorder) - 1)

# Example test case
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
binary_tree_from_preorder_inorder(preorder, inorder)

