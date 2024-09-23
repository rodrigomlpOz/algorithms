'''
https://leetcode.com/problems/is-graph-bipartite/
'''
import collections
def isBipartite(graph):
    color = {}
    def dfs(node):
        for nei in graph[node]:
            if nei in color:
               if color[nei] == color[node]:
                   return False
            else:
                color[nei] = 1 - color[node]
                if not dfs(nei):
                    return False
        return True

    
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(i):
                return False
    return True
        

graph1 = [[1,3], [0,2], [1,3], [0,2]]
graph2 = [[1,2,3], [0,2], [0,1,3], [0,2]]
isBipartite(graph2)

# from collections import deque

# def is_bipartite(graph):
#     color = {}
    
#     for node in graph:
#         if node not in color:  # Check unvisited nodes
#             queue = deque([node])
#             color[node] = 0  # Start coloring with 0
            
#             while queue:
#                 current = queue.popleft()
                
#                 for nei in graph[current]:
#                     if nei not in color:  # If the neighbor has not been colored
#                         color[nei] = 1 - color[current]  # Color with the opposite color
#                         queue.append(nei)
#                     elif color[nei] == color[current]:  # If neighbor has the same color
#                         return False
    
#     return True
