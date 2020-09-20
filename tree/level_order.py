# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([root])
        ans = []
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.extend([curr.left, curr.right])
            if level:
                ans.append(level)

        return ans