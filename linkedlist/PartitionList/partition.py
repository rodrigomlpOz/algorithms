class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    before_head = ListNode(0)  # Dummy node for nodes < x
    after_head = ListNode(0)   # Dummy node for nodes >= x

    before = before_head
    after = after_head

    current = head

    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    after.next = None         # Terminate the after list
    before.next = after_head.next  # Combine the two lists

    return before_head.next
