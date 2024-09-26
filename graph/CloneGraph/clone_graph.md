### Problem: Clone Graph (Leetcode 133)

The task is to **clone an undirected graph**. Each node in the graph contains a label and a list of its neighbors. The goal is to return a deep copy of the graph such that all nodes and edges are replicated.

#### Problem Description:

Given the `root` node of a connected undirected graph, return a **deep copy** of the graph. Each node in the graph contains:
- An integer value `label`.
- A list `edges` containing references to neighboring nodes.

### Input:
- A reference to the node `G` in the original graph.

### Output:
- A reference to the root node of the **cloned graph**, where each node and its neighbors are duplicated, maintaining the same structure as the original graph.

---

### Approach to Solution:

We can solve this using **Breadth-First Search (BFS)** or **Depth-First Search (DFS)**. Here we will focus on a BFS approach to clone the graph.

### Key Concepts:
1. **Cloning a node**: For each node in the original graph, create a corresponding node in the cloned graph.
2. **Preserving edges**: The cloned nodes must maintain the same connections as the original nodes.
3. **Mapping original to clone**: Use a dictionary to map each node in the original graph to its cloned counterpart.

### Solution Steps:
1. **Use BFS for graph traversal**: Start from the given node and traverse all its neighbors using a queue.
2. **Clone each node**: For each node, create a new node in the cloned graph.
3. **Use a dictionary to track clones**: Store the mapping between original and cloned nodes to avoid cloning a node multiple times.
4. **Maintain the connections**: For each original node, connect its neighbors to the corresponding cloned neighbors.

### Function Definition:

```python
import collections

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

def clone_graph(G):
    pass
```

- `GraphVertex`: Represents a node in the graph. Each node has a `label` and a list of `edges` (its neighbors).

### Function Call Examples:

1. **Graph 1: Triangle Graph**

**Graph Structure:**
```
   a ---- b
    \    /
     \  /
       c
```

- **Vertices:**
  - Node `a` is connected to `b` and `c`.
  - Node `b` is connected to `a` and `c`.
  - Node `c` is connected to `a` and `b`.

```python
# Creating the graph
a = GraphVertex("a")
b = GraphVertex("b")
c = GraphVertex("c")

# Connect the nodes
a.edges.extend([b, c])
b.edges.extend([a, c])
c.edges.extend([a, b])

# Clone the graph starting from node 'a'
cloned_a = clone_graph(a)

# Verifying the cloned graph
print(cloned_a.label)            # Expected Output: "a"
print(cloned_a.edges[0].label)   # Expected Output: "b"
print(cloned_a.edges[1].label)   # Expected Output: "c"
```

2. **Graph 2: Linear Chain**

**Graph Structure:**
```
   a ---- b ---- c
```

- **Vertices:**
  - Node `a` connects to `b`.
  - Node `b` connects to `a` and `c`.
  - Node `c` connects to `b`.

```python
# Creating the graph
a = GraphVertex("a")
b = GraphVertex("b")
c = GraphVertex("c")

# Connect the nodes
a.edges.append(b)
b.edges.extend([a, c])
c.edges.append(b)

# Clone the graph starting from node 'a'
cloned_a = clone_graph(a)

# Verifying the cloned graph
print(cloned_a.label)              # Expected Output: "a"
print(cloned_a.edges[0].label)     # Expected Output: "b"
print(cloned_a.edges[0].edges[1].label)  # Expected Output: "c"
```

3. **Graph 3: Single Node**

**Graph Structure:**
```
   a
```

- **Vertices:**
  - Node `a` has no neighbors.

```python
# Creating the graph
a = GraphVertex("a")

# Clone the graph starting from node 'a'
cloned_a = clone_graph(a)

# Verifying the cloned graph
print(cloned_a.label)  # Expected Output: "a"
print(cloned_a.edges)  # Expected Output: []
```

### High-Level Solution Overview:

1. **GraphVertex Class**: This class defines the structure of each node in the graph, having a label and a list of edges (neighbors).
2. **BFS Algorithm**:
   - Start by cloning the root node.
   - Use a BFS queue to traverse the graph, cloning nodes as they are encountered.
   - Ensure that each node is cloned only once by checking a dictionary that maps original nodes to their clones.
   - For each node, clone its neighbors and connect the corresponding cloned nodes via edges.
3. **Return** the cloned root node once the graph is fully cloned.

### Time Complexity:
- **Time Complexity**: O(V + E), where V is the number of vertices (nodes) and E is the number of edges. Each node and edge is visited once during the BFS traversal.

### Space Complexity:
- **Space Complexity**: O(V), where V is the number of nodes, for storing the cloned nodes in the dictionary and the BFS queue.

This approach ensures that all nodes and edges in the graph are cloned correctly.
