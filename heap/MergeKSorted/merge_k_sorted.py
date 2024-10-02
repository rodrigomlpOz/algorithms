from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    # Min-heap (priority queue) to store the head of each linked list
    heap = []
    
    # Define a comparison function for ListNode objects to compare based on their values
    for i, l in enumerate(lists):
        if l:
            heappush(heap, (l.val, i, l))  # Push tuple (value, list_index, node)
    
    # Dummy node to help construct the result list
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heappop(heap)  # Get the smallest node
        current.next = node  # Append the node to the result list
        current = current.next  # Move the current pointer
        
        # If the current list has more nodes, push the next node into the heap
        if node.next:
            heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next  # Return the merged list starting from dummy.next
