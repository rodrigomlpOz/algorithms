### Problem Statement
You are given a singly linked list, and you need to reverse the linked list using a recursive approach. The goal is to implement a function that reverses the linked list and returns the new head of the reversed list.

### Problem Definition
Given a singly linked list, implement a function `reverse` that recursively reverses the list and returns the new head node.

- **Input:**
  - A singly linked list with nodes containing integer data.
  
- **Output:**
  - The head of the reversed linked list.

### Function Signature
```python
def reverse(node: Node) -> Node:
```

### Example
```python
# Example:
# Input: Linked list: 85 -> 15 -> 4 -> 20
# Output: Reversed linked list: 20 -> 4 -> 15 -> 85
```

### High-Level Solution
1. **Base Case for Recursion:**
   - If the `node` is `None`, return `None` as there is nothing to reverse.
   - If the `node.next` is `None`, return `node` as it is the last node and becomes the new head of the reversed list.

2. **Recursive Case:**
   - Call `reverse(node.next)` to reverse the rest of the list and get the new head (`node1`) of the reversed list.
   - Adjust the pointers:
     - Set `node.next.next` to `node` to reverse the link.
     - Set `node.next` to `None` to terminate the original forward link.
   - Return the new head (`node1`).

3. **Handling the Linked List in the Main Code:**
   - Use a helper function `push` to add elements to the linked list.
   - Use the `printList` function to display the linked list before and after reversal.

### Time Complexity
- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. Each node is visited once.

- **Space Complexity:** O(n), due to the recursion stack in the worst case (if the linked list has `n` nodes).
