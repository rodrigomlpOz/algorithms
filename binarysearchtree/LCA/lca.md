class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

# Construct the nodes
node3 = BinaryTreeNode(data=3, size=1)
node12 = BinaryTreeNode(data=12, size=1)
node18 = BinaryTreeNode(data=18, size=1)
node5 = BinaryTreeNode(data=5, left=node3, size=2)
node15 = BinaryTreeNode(data=15, left=node12, right=node18, size=3)

# Root node
root = BinaryTreeNode(data=10, left=node5, right=node15, size=7)

# Now, root points to the root of the constructed binary tree
