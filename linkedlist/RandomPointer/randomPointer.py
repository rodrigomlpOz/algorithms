class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None  # Add random pointer to the Node class

def copyRandomList(head):
    if not head:
        return None

    old_to_new = {}
    current = head
    prev_copy = None

    # **First pass:** Create copies and assign 'next' pointers
    while current:
        copy = Node(current.val)
        old_to_new[current] = copy

        if prev_copy:
            prev_copy.next = copy  # Assign 'next' pointer of the previous copy

        prev_copy = copy
        current = current.next

    # **Second pass:** Assign 'random' pointers
    current = head
    while current:
        copy = old_to_new[current]
        if current.random:  # Explicit check for random pointer
            copy.random = old_to_new[current.random]  # Assign the copied random node
        current = current.next

    return old_to_new[head]
