class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the linked list in place as L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
    This function modifies the linked list in-place and returns nothing.
    """
    if not head or not head.next:
        return
    
    # Step 1: Find the middle of the linked list using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Split the list into two halves
    second_half = slow.next  # Start of the second half
    slow.next = None  # Cut the list to separate the first and second halves

    # Step 3: Reverse the second half
    prev, curr = None, second_half
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    # Now, `prev` is the head of the reversed second half

    # Step 4: Merge the two halves together
    first, second = head, prev
    while second:
        # Temporarily store the next pointers
        temp1, temp2 = first.next, second.next
        # Reorder the pointers
        first.next = second
        second.next = temp1
        # Move the pointers forward
        first = temp1
        second = temp2
