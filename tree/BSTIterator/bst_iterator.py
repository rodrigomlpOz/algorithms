# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        # Initialize by pushing the leftmost path from the root
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: TreeNode):
        # Push all the nodes from the leftmost path of the tree to the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top element of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # If the node has a right child, we need to process the leftmost path of that subtree
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        # If the stack is non-empty, then we have a next element
        return len(self.stack) > 0
