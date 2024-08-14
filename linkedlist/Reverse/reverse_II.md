### Problem Statement
You are given a singly linked list, represented by the head node. Your task is to reverse the linked list in place, such that the last node becomes the first node, the second last becomes the second node, and so on, until the first node becomes the last node.

### Problem Definition
Given a singly linked list, implement a function `reverse` within the `LinkedList` class that reverses the list in place. After reversing, the head should point to what was previously the last node.

- **Input:**
  - A linked list with the following nodes: `85 -> 15 -> 4 -> 20`.

- **Output:**
  - The reversed linked list: `20 -> 4 -> 15 -> 85`.

### Function Signature
```python
class LinkedList:
    def reverse(self): -> None
```

### Example
```python
# Example:
# Input: LinkedList with elements 85 -> 15 -> 4 -> 20
# Output: LinkedList reversed as 20 -> 4 -> 15 -> 85
```

### High-Level Solution
1. **Initialize Pointers:**
   - Initialize three pointers: `prev_node` as `None`, `current_node` as the head of the linked list, and `next_node` to track the next node in the list.

2. **Traverse and Reverse the List:**
   - While `current_node` is not `None`, perform the following steps:
     - Save the `next` node of `current_node` in `next_node`.
     - Reverse the link by setting `current_node.next` to `prev_node`.
     - Move `prev_node` to `current_node`.
     - Move `current_node` to `next_node`.

3. **Update the Head:**
   - After the loop ends, set the `head` of the linked list to `prev_node`, which will be the new head of the reversed list.

4. **Printing the List:**
   - A utility function `printList` is used to print the linked list, which traverses the list starting from the head and prints each node's data.

### Function Call Example
```python
# Example usage:
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print("Given Linked List:")
llist.printList() 

llist.reverse() 

print("\nReversed Linked List:")
llist.printList() 
```

### Time Complexity
- **Time Complexity:** O(n), where n is the number of nodes in the linked list. Each node is visited once.

- **Space Complexity:** O(1), since the list is reversed in place, requiring no additional space other than a few pointers.
