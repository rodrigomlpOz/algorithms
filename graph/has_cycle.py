class GraphVertex:
    def __init__(self, val):
        self.val = val
        self.edges = []

def has_cycle(node, visiting, visited):
    if node in visiting:
        return True
    visiting.add(node)
    for nei in node.edges:
        if nei not in visited and has_cycle(nei, visiting, visited):
            return True
    visiting.remove(node)
    visited.add(node)
    return False

def loop_graph(nodes):
    visiting = set()
    visited = set()
    for node in nodes:
        if node not in visited and has_cycle(a, visiting, visited):
            return True
    return False
a = GraphVertex(0)
b = GraphVertex(1)
c = GraphVertex(2)
d = GraphVertex(3)
e = GraphVertex(4)
a.edges.append(b)
b.edges.append(c)
c.edges.extend([d])
d.edges.append(e)
nodes = [a,b,c,d,e]
print(loop_graph(nodes))


print("hello")