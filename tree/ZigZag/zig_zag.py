# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        order = 1
        queue = collections.deque([root])
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    temp.append(curr.val)
                    queue.extend([curr.left, curr.right])
            if temp:
                if order == 1:
                    ans.append(temp)
                else:
                    ans.append(list(reversed(temp)))
                order ^= 1
        return ans
