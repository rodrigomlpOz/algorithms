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
def tree_lca(root, p, q):
    
    def is_lca(root, p, q):
        if not root:
            return (0, None)
        else:
            left = is_lca(root.left, p, q)
            if left[1] is not None:
                return left
            right = is_lca(root.right, p, q)
            if right[1] is not None:
                return right
            count_nodes = (1 if root == p or root == q else 0) + (left[0] if left[0] is not None else 0) + (right[0] if right[0] is not None else 0)
            found_lca = (True if count_nodes == 2 else None)
            return (count_nodes, root if found_lca else None)
    result = is_lca(root, p, q)[1] 
    return result  
      

root = TreeNode(0)
root.left = TreeNode(-3)
root.left.left = TreeNode(-10)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(3)
result = tree_lca(root, root.right.right, root.right.left.right)
print(result)

