class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    # Initialize two pointers, both starting at the head of the list
    slow = head
    fast = head
    
    # Traverse the list with the two pointers
    while fast and fast.next:
        slow = slow.next         # Move slow pointer one step
        fast = fast.next.next    # Move fast pointer two steps
        
        # If slow and fast pointers meet, there is a cycle
        if slow == fast:
            return True
    
    # If we reach the end of the list, there is no cycle
    return False
