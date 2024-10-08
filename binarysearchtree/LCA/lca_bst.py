# EPI 14.4 
def find_lca(tree, s, b):
    while tree:
        if s.data <= tree.data <= b.data:
            return tree  # Found the LCA
        elif tree.data < s.data:  # Move right if tree's data is smaller than s
            tree = tree.right
        else:  # Move left if tree's data is larger than b
            tree = tree.left
    return None  # Return None if no LCA is found

