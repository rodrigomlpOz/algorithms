# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = runner = head
        stack = []
        while runner and runner.next:
            stack.append(current.val)
            current = current.next
            runner = runner.next.next
        if runner != None:
            current = current.next
        while current:
            if current.val != stack.pop():
                return False
            current = current.next
        return True