# EPI 14.4 
def find_lca(tree, s, b):

    while tree.data < s.data or tree.data > b.data:
        # Keep searching since tree is outside of [s, b].
        while tree.data < s.data:
            tree = tree.right  # LCA must be in tree's right child.
        while tree.data > b.data:
            tree = tree.left  # LCA must be in tree's left child.
    # Now, s.data <= tree.data && tree.data <= b.data.
    return tree
