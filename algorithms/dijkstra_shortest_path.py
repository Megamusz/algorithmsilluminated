from collections import defaultdict

import math
from heap import Heap
import graph


class Graph(graph.Graph):
    def __init__(self, directed = True):
        self._graph = defaultdict(dict)
        self._directed = directed

    def add_edge(self, v1, v2, w):
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        if v2 in self._graph[v1]: #in case there're parallel edges from v1 -> v2, set the weight to minimun of them for shortest path problem
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
            max_node = 1
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                l = line.split()
                s = l[0]

                for e in l[1:]:
                    t, w = e.split(',')
                    self.add_edge(int(s), int(t), int(w))
                    max_node = max(max_node, max(int(s), int(t)))
               
            #Note: this is assuming we have all the vertexes from 1...max_node
            # In case any of the node not presenting in the text file, it is a separate node disconnect to the graph
            # that's why we need the following postprocessing pass to add those missing separated vertexes
            for i in range(1, max_node + 1):
                if i not in self._graph:
                    self.add_vertex(i)


def dijkstra_shortest_path_heap(graph, s):
    '''
    Dijkstra shortest path algorithm with Heap data structure. O((m+n)*logn)
    '''
    l = graph
    h = Heap()
    X = {s}
    A = {s:0}
    #initialize the heap
    for v in graph:
        if v not in X:
            score = l[s][v] if v in graph[s] else math.inf
            h.insert((score, v))

    while len(X) < len(graph):
        score, w = h.extract()
        A[w] = score

        X.add(w)
        
        for v in graph[w]:
            if v not in X:
                key = h.delete(v)
                key = min(key, A[w] + l[w][v])
                h.insert((key, v))
    
    return A  

def dijkstra_shortest_path(graph, s):
    '''
    Naive implementation of Dijkstra's shortest path algorithm. O(mn)
    '''
    X = {s} # vertices processed so far
    A = {s: 0} # computed shortest path distances 
    B = {s: [s]}
    l = graph 

    while len(X) < len(graph):
        min_cost = math.inf
        lvw = 0
        for v in X:
            for w in graph[v]:
                if w not in X:
                    if A[v] + l[v][w] < min_cost:
                        min_cost = A[v] + l[v][w]
                        vs = v
                        ws = w
                        lvw = l[v][w]

        if min_cost == math.inf:
            # assign vertices that can't reached from starting vertex with cost 1000000
            for v in graph:
                if v not in A:
                    A[v] = 1000000 
                    X.add(v)
        else:
            X.add(ws)
            A[ws] = A[vs] + lvw
            B[ws] = B[vs].copy()
            B[ws].append(ws)
            assert(A[ws] == min_cost)

    return A, B

def alg(filename):
    g = Graph()
    g.from_file(filename)
    # A, _ = dijkstra_shortest_path(g._graph, 1)
    A = dijkstra_shortest_path_heap(g._graph, 1)
    return '{},{},{},{},{},{},{},{},{},{}'.format(A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197])

def print_path(B):
    with open('path.txt', 'w') as f:
        for v in range(1, 201):
            path = B[v]
            print('{} => path => '.format(v), end='', file=f)
            for i, p in enumerate(path):
                print(p, end='', file=f)
                if i < len(path) -1:
                    print(' ,', end='', file=f)
                else:
                    print('', file=f)

if __name__ == '__main__':
   


    g = Graph()
    g.from_file('tests/problem9.8test.txt')

    A, B = dijkstra_shortest_path(g._graph, 1)
    A2 = dijkstra_shortest_path_heap(g._graph, 1)

    print(A)
    print(B)