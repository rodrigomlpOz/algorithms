### Problem: Topological Sorting and Cycle Detection in a Graph

The provided code is designed to detect cycles in a **directed graph**. It uses a **Depth-First Search (DFS)** approach to detect cycles by tracking the nodes currently being visited. If a node is encountered again during its DFS traversal, it indicates a cycle.

### High-Level Solution:

1. **Graph Representation**:
   - The graph is represented using the `GraphVertex` class, where each vertex (node) has a value (`val`) and a list of neighbors (`edges`).
   
2. **Cycle Detection**:
   - The `has_cycle` function performs a DFS traversal of the graph and checks whether any node is revisited during the traversal. If a node is revisited while still being processed, a cycle is detected.
   
3. **DFS Traversal**:
   - The graph is traversed node by node using DFS. Two sets are used to track the traversal:
     - `visiting`: Tracks the nodes that are currently being explored in the DFS call stack.
     - `visited`: Tracks nodes that have been fully explored to avoid reprocessing them.
     
4. **Cycle Check**:
   - The `loop_graph` function loops through all the nodes and calls the `has_cycle` function to check if any cycle exists in the graph. If a cycle is found, it returns `True`; otherwise, it returns `False`.

### Function Definitions:

#### 1. `has_cycle` Function:
This function checks if there is a cycle in the graph starting from a given node.

```python
def has_cycle(node, visiting, visited):
    """
    DFS function to detect a cycle starting from a given node.
    
    :param node: Current node being visited.
    :param visiting: Set of nodes being visited in the current DFS stack.
    :param visited: Set of nodes that have already been processed.
    :return: True if a cycle is detected, False otherwise.
    """
    if node in visiting:
        return True  # Cycle detected
    visiting.add(node)
    for nei in node.edges:
        if nei not in visited and has_cycle(nei, visiting, visited):
            return True
    visiting.remove(node)  # Remove the node from visiting after exploring its edges
    visited.add(node)  # Mark the node as fully visited
    return False  # No cycle detected
```

#### 2. `loop_graph` Function:
This function checks the entire graph for cycles by iterating through all the nodes and calling the `has_cycle` function.

```python
def loop_graph(nodes):
    """
    Function to detect if there's any cycle in the graph.
    
    :param nodes: List of graph nodes.
    :return: True if a cycle is detected, False otherwise.
    """
    visiting = set()
    visited = set()
    for node in nodes:
        if node not in visited and has_cycle(node, visiting, visited):
            return True  # Cycle detected
    return False  # No cycle detected
```

### Example Function Calls:

#### 1. Graph with No Cycles:

Graph Structure:
```
    a → b → c → d → e
```

```python
a = GraphVertex(0)
b = GraphVertex(1)
c = GraphVertex(2)
d = GraphVertex(3)
e = GraphVertex(4)

# Connecting the graph nodes
a.edges.append(b)
b.edges.append(c)
c.edges.append(d)
d.edges.append(e)

# List of all nodes
nodes = [a, b, c, d, e]

# Check for cycle in the graph
print(loop_graph(nodes))  # Expected Output: False (No cycle)
```

#### 2. Graph with a Cycle:

Graph Structure:
```
    a → b → c
        ↑   ↓
        e ← d
```

```python
a = GraphVertex(0)
b = GraphVertex(1)
c = GraphVertex(2)
d = GraphVertex(3)
e = GraphVertex(4)

# Connecting the graph nodes with a cycle
a.edges.append(b)
b.edges.append(c)
c.edges.append(d)
d.edges.append(e)
e.edges.append(b)  # This creates a cycle

# List of all nodes
nodes = [a, b, c, d, e]

# Check for cycle in the graph
print(loop_graph(nodes))  # Expected Output: True (Cycle detected)
```

### Explanation:

1. **DFS and Sets**:
   - The `visiting` set tracks nodes currently being explored. If a node is revisited while it’s still in the `visiting` set, a cycle is detected.
   - The `visited` set ensures that nodes are not processed more than once.
   
2. **Graph Traversal**:
   - The function `loop_graph` ensures that all nodes in the graph are checked for cycles, even if they are disconnected.

### Expected Outputs:
- For the first graph (no cycles), the output will be `False`.
- For the second graph (with a cycle), the output will be `True`.

This approach efficiently detects cycles in a directed graph using depth-first search and set-based tracking.
