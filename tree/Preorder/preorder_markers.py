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

#Alternative
# def reconstruct_preorder(preorder: List[Optional[int]]) -> Optional[BinaryTreeNode]:
#     """
#     Reconstructs a binary tree from its preorder traversal list with `None` as null markers
#     using a non-local index variable.

#     :param preorder: List of node values in preorder traversal, with `None` representing null nodes.
#     :return: The root of the reconstructed binary tree.
#     """
#     index = 0  # Initialize the index to track the current position in the preorder list

#     def buildTree() -> Optional[BinaryTreeNode]:
#         nonlocal index  # Allows modification of the 'index' variable from the enclosing scope

#         # Base Case: If all elements have been processed, return None
#         if index >= len(preorder):
#             return None

#         val = preorder[index]
#         index += 1  # Move to the next element for subsequent recursive calls

#         # If the current value is None, it signifies a null node
#         if val is None:
#             return None

#         # Create a new node with the current value
#         node = BinaryTreeNode(val)

#         # Recursively build the left and right subtrees
#         node.left = buildTree()
#         node.right = buildTree()

#         return node

#     return buildTree()
