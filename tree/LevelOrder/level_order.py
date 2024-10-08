# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def levelOrder(root):
    if not root:
        return []
    
    queue = deque([root])  # Initialize queue with root
    ans = []
    
    while queue:
        size = len(queue)    # Number of nodes at current level
        level = []
        for _ in range(size):
            curr = queue.popleft()
            level.append(curr.value)
            
            # Enqueue child nodes if they exist
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        ans.append(level)     # Add current level to answer
    
    return ans
