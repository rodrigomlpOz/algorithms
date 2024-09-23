'''
https://leetcode.com/problems/clone-graph/

'''
import collections

class GraphVertex:
    def __init__(self, label):
        self.label = label  # The unique identifier for the vertex
        self.edges = []     # List to store adjacent vertices (neighbors)

def clone_graph(G):
    if G is None:
        return None  # If the input graph is empty, return None

    # Initialize a queue for Breadth-First Search (BFS) and add the starting vertex
    q = collections.deque([G])
    
    # Dictionary to keep track of cloned vertices.
    # Keys are original vertices, and values are their corresponding clones.
    dictionary = {G: GraphVertex(G.label)}

    # Perform BFS to traverse the graph
    while q:
        # Dequeue the next vertex to process
        v = q.popleft()
        
        # Iterate through all neighbors of the current vertex
        for nei in v.edges:
            if nei not in dictionary:
                # Clone the neighbor if it hasn't been cloned yet
                dictionary[nei] = GraphVertex(nei.label)
                q.append(nei)  # Enqueue the neighbor for subsequent processing
            
            # Add the cloned neighbor to the edges of the cloned current vertex
            dictionary[v].edges.append(dictionary[nei])
    
    # Return the clone of the starting vertex
    return dictionary[G]

# class GraphVertex:
#     def __init__(self, label):
#         self.label = label
#         self.edges = []

# def clone_graph_dfs(node):
#     if not node:
#         return None
    
#     cloned_map = {}
    
#     def dfs(curr_node):
#         if curr_node in cloned_map:
#             return
        
#         # Clone the current node
#         cloned_map[curr_node] = GraphVertex(curr_node.label)
        
#         # Iterate through the neighbors
#         for nei in curr_node.edges:
#             dfs(nei)
#             cloned_map[curr_node].edges.append(cloned_map[nei])
    
#     dfs(node)
#     return cloned_map[node]