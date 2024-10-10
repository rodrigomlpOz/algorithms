from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        # Loop through all nodes at the current level
        for i in range(level_length):
            node = queue.popleft()
            # If it's the last node in this level, add to the result
            if i == level_length - 1:
                result.append(node.val)
            # Add left and right children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result
