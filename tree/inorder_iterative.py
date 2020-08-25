'''
Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

'''

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
#number of elements greater than 1
def inorder_recursive(root):
    stack = []
    ans = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        curr = stack.pop()
        ans.append(curr.val)
        root = curr.right
    return ans
        
    

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
inorder_recursive(root)
