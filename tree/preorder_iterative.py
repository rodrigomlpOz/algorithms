'''
9.8 EPI

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
def preorder_iterative(root):
    stack = []
    result = []

    if not root:
        return result

    curr_node = root
    while stack or curr_node:
        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
    return result

root = TreeNode(0)
root.left = TreeNode(-3)
root.right = TreeNode(9)
root.left.left = TreeNode(-10)
root.right.left = TreeNode(5)
preorder_iterative(root)

