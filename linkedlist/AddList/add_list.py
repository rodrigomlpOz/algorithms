# Adds list values
def add_list(L1, L2):
    place_iter = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.val if L1 else 0) + (L2.val if L2 else 0)
        L1 = L1.next if L1 else None 
        L2 = L2.next if L2 else None 
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val//10, place_iter.next
    return dummy_head.next
