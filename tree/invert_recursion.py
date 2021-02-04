'''
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
def invert_tree(root):
    def invertTree(root):
        if not root:
            return
        else:
            root.left =  invertTree(root.right)
            root.right = invertTree(root.left)
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

