import graph
from copy import copy, deepcopy

def vertex_cover(G, k):

    if len(G.edges) == 0:
        return True
    elif k == 0:
        return False

    u, v = next(iter(G.edges))

    Gu = deepcopy(G)
    Gu.remove(u)
    Gv = deepcopy(G)
    Gv.remove(v)

    return vertex_cover(Gu, k-1) or vertex_cover(Gv, k-1)

class Graph(graph.Graph):
    def __init__(self):
        self.edges = set()
        super().__init__(directed=False)

    def add_edge(self, v1, v2):
        self.edges.add((v1, v2))
        super().add_edge(v1, v2)

    def remove(self, v):
        for u in self._graph[v]:
            if (u, v) in self.edges:
                self.edges.remove((u, v))
            if (v, u) in self.edges:
                self.edges.remove((v, u))
        super().remove(v)

if __name__ == '__main__':
    G = Graph()

    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)

    print(vertex_cover(G, k=3))