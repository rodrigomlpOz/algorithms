class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to reverse a linked list
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

# Main function to check if the list is a palindrome
def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    second_half = reverse_list(slow)

    # Step 3: Compare the first half with the reversed second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
