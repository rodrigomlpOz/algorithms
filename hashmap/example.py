#merge k sorted lists skeleton in python
def merge_k_sorted_lists(lists):
    pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create input linked lists
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

# Create the list of linked lists
lists = [list1, list2, list3]

