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
    ans = []

    if not root:
        return ans

    curr_node = root
    prev_node = None 

    while  stack or  curr_node:
        if curr_node:
            ans.append(curr_node.val)
            stack.append(curr_node)
            curr_node = curr_node.left 
        else:
            prev_node = stack.pop()
            curr_node = prev_node.right

    print(ans)

root = TreeNode(0)
root.left = TreeNode(-3)
root.right = TreeNode(9)
root.left.left = TreeNode(-10)
root.right.left = TreeNode(5)
preorder_iterative(root)

