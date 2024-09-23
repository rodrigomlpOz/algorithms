class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node in the linked list


def cyclically_right_shift_list(L, k):

    if L is None:
        return L

    # Computes the length of L and the tail.
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L

    tail.next = L  # Makes a cycle by connecting the tail to the head.
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head

# Helper function to convert a list to a linked list
def list_to_linkedlist(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linkedlist(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))
# Example 1:
L1 = list_to_linkedlist([1, 2, 3, 4, 5])
k1 = 2
result1 = cyclically_right_shift_list(L1, k1)
print("Example 1:")
print_linkedlist(result1)  # Output: 4 -> 5 -> 1 -> 2 -> 3

# Example 2:
L2 = list_to_linkedlist([1, 2, 3, 4, 5])
k2 = 7
result2 = cyclically_right_shift_list(L2, k2)
print("Example 2:")
print_linkedlist(result2)  # Output: 4 -> 5 -> 1 -> 2 -> 3