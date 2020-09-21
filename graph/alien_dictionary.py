class Solution(object):
    def add_vertices(self, w, graph):
        for ch in w:
            if ch not in graph:
                graph[ch] = set([])        
        return
    
    def add_words_to_graph(self, graph, w1, w2):
        self.add_vertices(w1, graph)
        self.add_vertices(w2, graph)        
        min_length = min(len(w1), len(w2))
        found = False
        for i in range(min_length):
            if w1[i] != w2[i]:
                graph[w1[i]].add(w2[i])
                found = True
                break
        if found == False and len(w1) > len(w2):
            return False # "abstract", "abs" is an error. But "abs", "abstract" is perfectly fine.
        return True

    def build_graph(self, words):
        graph = {}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if not self.add_words_to_graph(graph, w1, w2):
                return {}
        self.add_vertices(words[-1], graph)
        return graph

    def topo_dfs(self, x, graph, visited, visiting, ans): # Return True if there is a cycle
        if x in visiting:
            return True
        visiting.add(x)
        for nei in graph[x]:
            if nei not in visited and self.topo_dfs(nei, graph, visited, visiting, ans):
                return True
        visiting.remove(x)
        ans.append(x)
        visited.add(x)
        return False

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == []:
            return ""
        graph = self.build_graph(words)
        visited, visiting, st = set([]), set([]), []
        for k in graph.keys():
            if k not in visited and self.topo_dfs(k, graph, visited, visiting, st):
                    return ""
        st.reverse()
        return "".join(st)