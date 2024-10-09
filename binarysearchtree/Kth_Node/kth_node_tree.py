#EPI 9.9
#"Find the k-th Node in an In-Order Traversal of a Binary Tree"

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree, k):
    if not tree:
        return None  # Base case when the tree is empty
    
    left_size = tree.left.size if tree.left else 0  # Calculate left subtree size
    
    if left_size + 1 == k:
        # Current node is the k-th node
        return tree.data
    elif left_size + 1 < k:
        # k-th node is in the right subtree
        # We skip the left subtree and the current node
        return find_kth_node_binary_tree(tree.right, k - (left_size + 1))
    else:
        # k-th node is in the left subtree
        return find_kth_node_binary_tree(tree.left, k)
