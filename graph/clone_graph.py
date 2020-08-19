import collections
class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

def clone_graph(G):
    q = collections.deque([G])
    dictionary = {G:GraphVertex(G.label)}

    while q:
        v = q.popleft()
        for nei in v.edges:
            if nei not in dictionary:
                dictionary[nei] = GraphVertex(nei.label)
                q.append(nei)
            dictionary[v].edges.append(dictionary[nei])
    return dictionary[G]

a = GraphVertex("a")
b = GraphVertex("b")
c = GraphVertex("c")
a.edges.extend([b, c])
clone_graph(a)