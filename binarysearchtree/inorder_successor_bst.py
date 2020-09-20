# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')
        
        # inorder traversal : left -> node -> right
        while stack or root:
            # 1. go left till you can
            if root:
                stack.append(root)
                root = root.left
            else:
                # 2. all logic around the node
                root = stack.pop()
                if inorder == p.val:    # if the previous node was equal to p
                    return root         # then the current node is its successor
                inorder = root.val

                # 3. go one step right
                root = root.right

        # there is no successor
        return None