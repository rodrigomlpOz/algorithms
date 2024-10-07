'''
PROBLEM STATEMENT: 9.5 on EPI p.119
'''

def sum_root_to_leaf(tree):
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            return 0

        partial_path_sum = partial_path_sum * 2 + tree.data
        if not tree.left and not tree.right:  # Leaf.
            return partial_path_sum
        # Non-leaf.
        return (sum_root_to_leaf_helper(tree.left, partial_path_sum) +
                sum_root_to_leaf_helper(tree.right, partial_path_sum))
    sum_root_to_leaf_helper(tree, 0)
