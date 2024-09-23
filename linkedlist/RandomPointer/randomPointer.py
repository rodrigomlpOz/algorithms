class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def copyRandomList(head):
    if not head:
        return None

    old_to_new = {}
    current = head
    prev_copy = None

    # **First pass:** Create copies and assign 'next' pointers
    # at the time you encounter a node, the random pointer of 
    # that node could point to another node further in the list, whose copy has not yet been created.
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
        copy.random = old_to_new.get(current.random)
        current = current.next

    return old_to_new[head]
