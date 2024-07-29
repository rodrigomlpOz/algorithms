class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_preorder(preorder):
    def reconstruct_preorder_helper(preorder_iter):
        # Fetch the next value from the iterator. If the iterator is exhausted, return None.
        # This ensures that the function gracefully handles the end of the traversal list.
        subtree_key = next(preorder_iter, None)
        
        if subtree_key is None:
            return None

        # Construct the left and right subtrees using the next elements in the iterator.
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct_preorder_helper(iter(preorder))
