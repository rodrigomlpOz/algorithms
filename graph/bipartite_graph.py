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