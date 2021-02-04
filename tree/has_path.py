'''
PROBLEM STATEMENT: https://leetcode.com/problems/path-sum/
'''

def has_path_sum(tree, remaining_weight):

    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf.
        return remaining_weight == tree.data
    # Non-leaf.
    return (has_path_sum(tree.left, remaining_weight - tree.data)
            or has_path_sum(tree.right, remaining_weight - tree.data))
