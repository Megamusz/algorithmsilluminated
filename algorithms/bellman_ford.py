import math
from collections import defaultdict
import dijkstra_shortest_path

def bellman_ford(G, s):
    n = len(G._graph)
    Ai_1 = [0 for i in range(n + 1)]
    Ai = [0 for i in range(n+1)]

    Bi_1 = [None for i in range(n+1)] #used for reconstruction, each B[i, v] is the 2nd to last vertex on a shortest path s-> v with at most i edges
    Bi = [None for i in range(n+1)] 
    c = G._graph

    for v in range(1, n+1):
        Ai_1[v] = 0 if v == s else math.inf

    for i in range(1, n): #edge buget
        for v in range(1, n+1):
            case1 = Ai_1[v] #P has <= i-1 edges
            case2 = math.inf

            for w in G._in[v]:  #P has i edges with last hop (w, v), then P' is a shortest s-w path with <= i-1 edges
                if case2 > Ai_1[w] + c[w][v]:
                    case2 = Ai_1[w] + c[w][v]
                    Bi[v] = w 

            if case1 < case2:
                Ai[v] = case1
                Bi[v] = Bi_1[v]
            else:
                Ai[v] = case2

        Ai, Ai_1 = Ai_1, Ai
        Bi, Bi_1 = Bi_1, Bi

    return Ai_1[1:n+1], Bi_1[1:]


class Graph(dijkstra_shortest_path.Graph):
    '''
    Graph structure enhanced with _in dict to record the incomming vertices for each vertex,
    this is required in the reconstruction setup 
    '''
    def __init__(self, directed = True):
        self._in = defaultdict(set)
        super().__init__(directed=True)

    def add_edge(self, v1, v2, w):
        self._in[v2].add(v1)
        super().add_edge(v1, v2, w)


if __name__ == '__main__':
    g = Graph()
    g.from_file('tests/problem9.8test.txt')
    s = 1
    A, B = bellman_ford(g, s)
    print(A, B)

    path = {1: [1]}
    for v in range(1, len(g._graph) + 1):
        if v == s:
            continue
        w = v
        path[v] = [v]
        while B[w-1] != 1:
            w = B[w-1]
            path[v].insert(0, w)
        path[v].insert(0, s)

    print(path)
