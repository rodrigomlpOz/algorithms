#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        
        tmp = head
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        if l1 is None:
            l1 = l2
        while l1:
            tmp.next = ListNode(l1.val)
            l1 = l1.next
            tmp = tmp.next
        
        return head.next