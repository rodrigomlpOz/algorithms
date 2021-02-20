'''

PROBLEM STATEMENT: 9.2 EPI

    1
   / \
  2   2
 / \ / \
3  4 4  3

'''
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
def is_symmetric(root):
    if not root:
        return True
    def symmetry(left_node, right_node):
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False
        else:
            return (left_node.val == right_node.val) and symmetry(left_node.left, right_node.right) and symmetry(left_node.right, right_node.left)
    return symmetry(root.left, root.right) 
      

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
result = is_symmetric(root)
print(result)

