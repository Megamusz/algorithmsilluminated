from collections import defaultdict
import queue
import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, directed=True):
        self._graph = defaultdict(set)
        self._directed = directed
        self._visited = set()

    def from_file(self, file):
        with open(file, 'r') as f:
            max_node = 1
            for line in f.readlines():
                if not line.strip():
                    continue
                v1, v2 = line.strip().split()
                max_node = max(max_node, max(int(v1), int(v2)))
                self.add_edge(int(v1), int(v2))

            #Note: this is assuming we have all the vertexes from 1...max_node
            # In case any of the node not presenting in the text file, it is a separate node disconnect to the graph
            # that's why we need the following postprocessing pass to add those missing separated vertexes
            for i in range(1, max_node + 1):
                if i not in self._graph:
                    self.add_vertex(i)

    def add_vertex(self, v):
        if v not in self._graph:
            self._graph[v] 

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self._graph[v1].add(v2) 
        if not self._directed:
            self._graph[v2].add(v1)

    def remove(self, v):
        for v1, v2s in self._graph.items():
            if v in v2s:
                v2s.remove(v)
        
        del self._graph[v]

    def n_vertex(self):
        return len(self._graph)

    def BFS(self, s):
        visited = {s}
        q = queue.Queue()
        q.put(s)

        while not q.empty():
            v = q.get()

            for w in self._graph[v]:
                if w not in visited:
                    #mark w as explored
                    visited.add(w)
                    #add w to Q (at the end)
                    q.put(w)

    def DFS(self, s):
        visited = {s}
        stack = queue.LifoQueue()
        stack.put(s)

        while not stack.empty():
            v = stack.get()
            # print(v, end='->')
            for w in self._graph[v]:
                if w not in visited:
                    #mark w as explored
                    visited.add(w)
                    #add w to the stack (at the front)
                    stack.put(w)

   
    def topolocial_sort(self):
        self._visited.clear()
        self._fs = {}
        self._current_label = len(self._graph)

        for v in self._graph:
            if v not in self._visited:
                self.DFS_recursive(v)


    def DFS_recursive(self, s):
        self._visited.add(s)

        for v in self._graph[s]:
            if v not in self._visited:
                self.DFS_recursive(v)
        
        self._fs[s] = self._current_label
        self._current_label -= 1

   

    


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

if __name__ == '__main__':
    # g = Graph(directed = False)

    # g.add_edge('s', 'a')
    # g.add_edge('s', 'b')
    # g.add_edge('a', 'c')
    # g.add_edge('b', 'c')
    # g.add_edge('b', 'd')
    # g.add_edge('c', 'd')
    # g.add_edge('c', 'e')
    # g.add_edge('e', 'd')

    g = Graph(directed = True)
    g.from_file('tests/problem8.10.txt')

    # g.add_edge('s', 'v')
    # g.add_edge('s', 'w')
    # g.add_edge('v', 't')
    # g.add_edge('w', 't')

    # print(g)
    # print(g.reverse())
    g.kosaraju_scc()

    # g.BFS('s')
    # g.DFS('s')
    # g.topolocial_sort()
    # print(g._fs)

    G = nx.DiGraph(g._graph)

    nx.draw_networkx(G)
    plt.show()