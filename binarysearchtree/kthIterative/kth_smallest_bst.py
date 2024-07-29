class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
#number of elements greater than 1
def kth_smallest_bst(root, k):
  stack = []
  while root or stack:
      if root:
          stack.append(root)
          root = root.left
      else:
          root = stack.pop()
          k -= 1
          if k == 0:
              return root.val
          root = root.right
        
    

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
kth_smallest_bst(root, 3)
