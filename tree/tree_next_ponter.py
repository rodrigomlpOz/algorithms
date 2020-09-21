# Definition for binary tree with next pointer.
class TreeLinkNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    

import collections
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        q = collections.deque([root])
        while q:
            node1 = q.popleft()
            if node1 and node1.left:
                node1.left.next = node1.right
                q.append(node1.left)
            if node1 and node1.right:
                if node1.next:
                    node1.right.next = node1.next.left
                else:
                    node1.right.next = None

                q.append(node1.right)