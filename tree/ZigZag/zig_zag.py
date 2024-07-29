from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level_values.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level_values:
                if not left_to_right:
                    level_values.reverse()
                result.append(level_values)
                
            left_to_right = not left_to_right
        
        return result
