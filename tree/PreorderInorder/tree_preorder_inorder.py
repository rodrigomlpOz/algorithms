from typing import List, Optional

class TreeNode:
    def __init__(self, value: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Create a dictionary to map each value to its index in the inorder traversal.
    value_to_inorder_index = {value: index for index, value in enumerate(inorder)}

    def construct_tree(preorder_start: int, preorder_end: int,
                       inorder_start: int, inorder_end: int) -> Optional[TreeNode]:
        # Base case: if the range is invalid, return None (no tree to construct).
        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return None

        # The first element in the current preorder range is the root of the subtree.
        root_value = preorder[preorder_start]
        root_inorder_index = value_to_inorder_index[root_value]
        left_subtree_size = root_inorder_index - inorder_start

        # Create the root node with the identified value.
        root = TreeNode(value=root_value)

        # Recursively build the left subtree.
        root.left = construct_tree(
            preorder_start + 1,
            preorder_start + 1 + left_subtree_size,
            inorder_start,
            root_inorder_index
        )

        # Recursively build the right subtree.
        root.right = construct_tree(
            preorder_start + 1 + left_subtree_size,
            preorder_end,
            root_inorder_index + 1,
            inorder_end
        )

        return root

    # Start the construction from the full range of preorder and inorder traversals.
    return construct_tree(preorder_start=0, preorder_end=len(preorder),
                          inorder_start=0, inorder_end=len(inorder))
