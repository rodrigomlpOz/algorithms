'''

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
def height_balanced(root):
    
    def is_balanced(root):
        if not root:
            return (-1, True)
        else:
            left = is_balanced(root.left)
            if left[1] == False:
                return (0, False)
            right = is_balanced(root.right)
            if right[1] == False:
                return (0, False)
            curr_height = 1 + max(left[0], right[0])
            node_balanced = abs(left[0] - right[0]) <= 1
            return (curr_height, node_balanced)
    result = is_balanced(root)[1]  
    return result  
      

root = TreeNode(0)
root.left = TreeNode(-3)
root.left.left = TreeNode(-10)
result = height_balanced(root)
print(result)

