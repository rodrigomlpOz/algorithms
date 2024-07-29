class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def height_balanced(root):
    def check_balance(node):
        if not node:
            return 0, True  # A null tree is balanced with height 0

        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)

        # The current node is balanced if the left and right subtrees are balanced
        # and the difference in their heights is not more than 1
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        current_height = 1 + max(left_height, right_height)

        return current_height, current_balanced

    _, is_balanced = check_balance(root)
    return is_balanced

# Example usage
root = TreeNode(0)
root.left = TreeNode(-3)
root.left.left = TreeNode(-10)
root.right = TreeNode(9)
root.right.left = TreeNode(5)

result = height_balanced(root)
print(result)  # Output: True (indicating the tree is balanced)
