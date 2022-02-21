'''
PROBLEM STATEMENT: https://leetcode.com/problems/invert-binary-tree/
    1
   / \
  2   3
 / \ / \
4  5 6  7

'''
import collections
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def invertTree(root):
    if not root:
        return None
    else:
        #swap left and right subtrees
        root.left,root.right = root.right,root.left

        #recursively solve the problem
        if root.left:
            invertTree(root.left)
        if root.right:
            invertTree(root.right)

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = invert_tree(root)
print(result)

