#EPI 14.5
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size
        
def bstFromPreorder(preorder_sequence):

    if not preorder:
            return None
    root = BinaryTreeNode(preorder[0])
    i = 1
    while i<len(preorder) and  preorder[i] < root.val:
        i+=1
    root.left = bstFromPreorder(preorder[1:i])
    root.right = bstFromPreorder(preorder[i:])
    return root
