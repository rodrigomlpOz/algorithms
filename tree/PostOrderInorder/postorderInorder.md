### Problem Definition:
Given two integer arrays `inorder` and `postorder`, where:
- `inorder` is the inorder traversal of a binary tree.
- `postorder` is the postorder traversal of the same binary tree.

Construct and return the binary tree from these traversals.

### Function Definition:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_inorder_postorder(inorder, postorder):
    pass
```

### Example Function Calls:

**Example 1:**
```python
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = construct_binary_tree_from_inorder_postorder(inorder, postorder)
```
Expected Output Tree:
```
        3
       / \
      9   20
         /  \
        15   7
```

**Example 2:**
```python
inorder = [-1]
postorder = [-1]

root = construct_binary_tree_from_inorder_postorder(inorder, postorder)
```
Expected Output Tree:
```
  -1
```

### High-Level Solution:

1. **Tree Structure:**
   - In the **postorder traversal**, the last element is always the **root** of the tree.
   - In the **inorder traversal**, elements to the left of the root are part of the **left subtree**, and elements to the right of the root are part of the **right subtree**.

2. **Recursion:**
   - Find the root of the tree by taking the last element from `postorder`.
   - Use the `inorder` array to determine which nodes are in the left and right subtrees by finding the position of the root in the `inorder` list.
   - Recursively build the left and right subtrees by slicing the `inorder` and `postorder` arrays accordingly.

3. **Base Case:**
   - When the `inorder` or `postorder` array is empty, return `None`.

### Step-by-Step:
1. The last element of `postorder` is the root.
2. Find this root in the `inorder` array.
3. Elements left of the root in `inorder` form the left subtree; elements right of the root form the right subtree.
4. Recursively construct left and right subtrees using updated slices of `inorder` and `postorder`.
5. Return the constructed root.

This approach ensures the tree is constructed in O(n) time where n is the number of nodes, as each element is visited once during the traversal.

Let me explain this step by step, using both **postorder** and **inorder** traversal orders to help you understand why we process the **right subtree first** when constructing a binary tree from **postorder** and **inorder** lists.

### Postorder Traversal:
- In **postorder traversal**, nodes are visited in this order: **left subtree, right subtree, root**.
- So, the root of the tree comes **last** in the postorder list.

### Inorder Traversal:
- In **inorder traversal**, nodes are visited in this order: **left subtree, root, right subtree**.
- The position of the root in the `inorder` array allows us to split the tree into **left** and **right** subtrees.

### Why Build the Right Subtree First?

The **postorder** traversal tells us:
1. The **root** of the current subtree is always the last element in the postorder list.
2. The **right subtree** appears immediately **before the root** in postorder.

### Let's Walk Through an Example:

Consider the following example:

#### Given Traversals:
- **Inorder**: [9, 3, 15, 20, 7]
- **Postorder**: [9, 15, 7, 20, 3]

1. **Step 1**: Identify the **root**:
   - The last element in `postorder` is `3`, so the root is `3`.

2. **Step 2**: Split the **inorder** list using the root:
   - From the `inorder` list, we find that `3` splits the list into:
     - **Left subtree**: [9]
     - **Right subtree**: [15, 20, 7]

3. **Step 3**: Determine the subtrees in **postorder**:
   - The postorder traversal should visit the left subtree, right subtree, and then the root. So the postorder array looks like this:
     - `[9]` (left subtree),
     - `[15, 7, 20]` (right subtree),
     - `3` (root).

4. **Step 4**: Build the **right subtree first**:
   - We know that the last part of the postorder list before the root is the **right subtree** (`[15, 7, 20]`), so we build this subtree first.

#### Right Subtree Construction:
- The next element in `postorder` (before `3`) is `20`, so `20` is the root of the right subtree.
- From the `inorder` list, `20` splits its subtree into:
  - **Left**: [15]
  - **Right**: [7]

Now, we repeat the process:
- The next element in postorder is `7`, so `7` is the root of the right subtree of `20`.
- The next element in postorder is `15`, so `15` is the left subtree of `20`.

#### Left Subtree Construction:
- Finally, we construct the left subtree for the root `3`, which is simply `[9]`.

### Tree Construction:
After following the steps above, the tree we get is:

```
        3
       / \
      9   20
         /  \
        15   7
```

### Why **Right Comes First** in Postorder Construction:
- In postorder traversal, the root is always the **last** element, and the **right subtree** comes immediately **before** the root.
- So, to build the tree correctly, you need to process the right subtree **before** the left subtree, because of the way postorder traversal works (left, right, root).

If you tried to build the **left subtree first**, you would encounter issues because you would be processing elements that belong to the right subtree too early.

### Key Point to Remember:
- **Postorder** traversal gives you the **root last**, but just before the root, it gives you the **right subtree**. That's why, when constructing the tree from postorder, you need to build the right subtree first, then the left subtree, and finally attach the root.

Let me know if you want further clarification or need to see another example!