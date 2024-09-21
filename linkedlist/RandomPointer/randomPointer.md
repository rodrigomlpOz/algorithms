**Problem Statement:**

You are given a linked list where each node contains:

- An integer `val`.
- A pointer `next` to the next node.
- A pointer `random` that can point to any node in the list or be `null`.

Your task is to **create a deep copy** of this linked list. The copied list should consist of entirely new nodes, with the `next` and `random` pointers set up in the same way as in the original list.

---

**Function Definition:**

```python
def copyRandomList(head):
    pass  # Function to copy the linked list with random pointers
```

---

**Sample Calls with Print Statements:**

First, let's define a `Node` class and create a sample linked list to work with.

```python
# Definition for a Node.
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val          # The value of the node
        self.next = next        # Pointer to the next node
        self.random = random    # Pointer to a random node
```

Now, create a sample linked list:

```python
# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Setting up 'next' pointers
node1.next = node2
node2.next = node3

# Setting up 'random' pointers
node1.random = node3    # Node 1's random pointer points to Node 3
node2.random = node1    # Node 2's random pointer points to Node 1
node3.random = node3    # Node 3's random pointer points to itself
```

Call the `copyRandomList` function and print the results:

```python
# Copying the list
copied_head = copyRandomList(node1)

# Function to print the list for verification
def printList(head):
    current = head
    while current:
        print(f"Node value: {current.val}")
        if current.random:
            print(f"Random points to: {current.random.val}")
        else:
            print("Random points to: None")
        current = current.next
    print("---")

print("Original list:")
printList(node1)

print("Copied list:")
printList(copied_head)
```

---

**High-Level Solution:**

To solve this problem, we need to create an exact replica of the original linked list, ensuring that both the `next` and `random` pointers in the copied list point to the appropriate nodes. Here’s a high-level overview of how to achieve this:

1. **Create a Mapping from Original Nodes to Copied Nodes:**

   - **Objective:** Keep track of each original node and its corresponding copied node.
   - **Method:**
     - Traverse the original list.
     - For each node, create a new node with the same value.
     - Use a hash map (dictionary) to map the original node to the copied node.

2. **Assign `next` Pointers to the Copied Nodes:**

   - **Objective:** Set up the `next` pointers in the copied list to mirror the original list.
   - **Method:**
     - Traverse the original list again.
     - For each original node, set the `next` pointer of its copied node to point to the copied version of the original node's `next`.
     - Use the mapping to find the copied nodes.

3. **Assign `random` Pointers to the Copied Nodes:**

   - **Objective:** Set up the `random` pointers in the copied list to mirror the original list.
   - **Method:**
     - Traverse the original list once more.
     - For each original node, set the `random` pointer of its copied node to point to the copied version of the original node's `random`.
     - Again, use the mapping to find the copied nodes.

4. **Return the Head of the Copied List:**

   - **Objective:** Provide the entry point to the new copied list.
   - **Method:**
     - Return the copied node that corresponds to the original list's head node using the mapping.

**Key Concepts:**

- **Hash Map (Dictionary):**
  - Utilized to maintain a relationship between each original node and its copied node.
  - Enables quick lookup when assigning `next` and `random` pointers.

- **Deep Copy vs. Shallow Copy:**
  - A **deep copy** creates new instances of the nodes, and the copied nodes do not share references with the original nodes.
  - A **shallow copy** would copy the nodes but maintain references to the original `next` and `random` nodes, which is not desired here.

**Benefits of This Approach:**

- **Simplicity:**
  - The logic is straightforward and easy to follow.
  - Each step has a clear purpose.

- **Correctness:**
  - Ensures that all `next` and `random` pointers in the copied list point to the correct copied nodes.
  - Handles cases where `random` pointers are `null` or point to nodes not yet copied.

- **Maintainability:**
  - The use of a mapping simplifies the pointer assignments.
  - The code can be easily extended or modified if additional pointers or properties are added to the nodes.

**Considerations:**

- **Time Complexity:** O(N), where N is the number of nodes in the list.
  - Each traversal goes through all nodes, but the number of traversals is constant.

- **Space Complexity:** O(N), due to the extra space used by the mapping.
  - Necessary to maintain the relationships between original and copied nodes.

**Alternative Approaches:**

- **Interweaving Nodes (O(1) Space):**
  - An advanced method that involves inserting copied nodes into the original list and then separating them.
  - More complex and harder to implement correctly.
  - May not be suitable under time constraints or in an interview setting.

**Conclusion:**

By following this high-level approach, you can create a deep copy of a linked list with random pointers. The key is to maintain a mapping between the original nodes and their copies to accurately assign the `next` and `random` pointers in the copied list.

---

**Note:** The actual implementation details (code) are omitted as per your request. This explanation provides a clear understanding of the strategy to solve the problem without delving into the code itself.