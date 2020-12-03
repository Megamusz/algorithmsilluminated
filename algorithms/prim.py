
from collections import defaultdict
import math 
from heap import Heap

def prim(graph):
    '''
    Assuming graph is represented by dict of dict, e.g. 
    {1: {2: 200}, 2: {1: 200}, 1: {3: 100}, 3: {1: 100}}
    this means cost of 1 <-> 2 is 200 and cost of 1 <->3 is 100
    note the graph is undirected here
    
    Brief of Prim's algorithm:

    Initialize X = {s} [s is arbitrarily chosen from V]
    T = empty set [invariant: X = vertices spanned by tree T so far]
    while X != V
        Let e = (u, v) be the cheapest edge of G with u in X and v not in X
        Add e to T, Add v to X
    '''

    X = {1} 
    T = set()
    c = graph
    total_cost = 0

    while len(X) < len(graph):
        min_cost = math.inf
        edge = None

        for u in X:
            for v in graph[u]:
                if v not in X:
                    if c[u][v] < min_cost:
                        min_cost = c[u][v]
                        edge = (u, v)

        
        T.add(edge)
        X.add(edge[1])

        total_cost += min_cost
    
    return total_cost

def prim_heap(graph):
    c = graph
    h = Heap()
    X = {1}
    T = set()
    total_cost = 0

    #initialize the heap
    for v in graph:
        key = c[1][v] if v in graph[1] else math.inf
        h.insert((key, v))

    while len(X) < len(graph):
        key, w = h.extract()
        total_cost += key
        X.add(w)

        for v in graph[w]:
            if v not in X:
                key = h.delete(v)
                key = min(key, c[w][v])
                h.insert((key, v))
            
    return total_cost

class Graph(object):
    def __init__(self, directed = True):
        self._graph = defaultdict(dict)
        self._directed = directed

    def add_vertex(self, v):
        if v not in self._graph:
            self._graph[v] = {}

    def add_edge(self, v1, v2, w):
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        if v2 in self._graph[v1]: #in case there're parallel edges from v1 -> v2, set the weight to minimun of them 
            self._graph[v1][v2] = min(self._graph[v1][v2], w)
        else: 
            self._graph[v1][v2] = w

        if not self._directed:
            if v1 in self._graph[v2]:
                self._graph[v2][v1] = min(self._graph[v2][v1], w)
            else:
                self._graph[v2][v1] = w

    def from_file(self, filename):
        with open(filename, 'r') as f:
            n_node, n_edge = f.readline().strip().split()

            for i in range(1, int(n_node) + 1):
                self.add_vertex(i)

            for i in range(int(n_edge)):
                start, end, cost = f.readline().strip().split()
                self.add_edge(int(start), int(end), int(cost))


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def alg(filename):
    g = Graph(directed=False)
    g.from_file(filename)
    return prim_heap(g._graph)


if __name__ == '__main__':
    
    g = Graph(directed= False)
    g.from_file('tests/input_random_1_10.txt')
    print(g)
    print(g._graph[1])

    print(prim_heap(g._graph))