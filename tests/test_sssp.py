import unittest
from algorithms.dijkstra_shortest_path import dijkstra_shortest_path_heap, dijkstra_shortest_path, Graph
import bellman_ford

class TestDijkstra(unittest.TestCase):
    def test_case_dijkstra(self):
        g = Graph(directed = True)
        g.from_file('tests/problem9.8test.txt')
        A = dijkstra_shortest_path_heap(g._graph, s=1)
        self.assertEqual([A[i] for i in range(1, 9)], [0, 1, 2, 3, 4, 4, 3, 2])
    
    def test_case_bellmanford(self):
        g = bellman_ford.Graph(directed = True)
        g.from_file('tests/problem9.8test.txt')
        A, B = bellman_ford.bellman_ford(g, s=1)
        self.assertEqual(A, [0, 1, 2, 3, 4, 4, 3, 2])

    def test_case_consistency(self):
        g = bellman_ford.Graph(directed = True)
        g.from_file('tests/problem9.8test.txt')
        s = 1
        _, B = bellman_ford.bellman_ford(g, s)
    
        #reconstruct the path from bellmanford algorithm and compare to the one derived from dijkstra
        path1 = {s: [s]}
        for v in range(1, len(g._graph) + 1):
            if v == s:
                continue
            w = v
            path1[v] = [v]
            while B[w-1] != s:
                w = B[w-1]
                path1[v].insert(0, w)
            path1[v].insert(0, s)

        _, path2 = dijkstra_shortest_path(g._graph, s)
        
        for v in range(1, len(g._graph) + 1):
            self.assertEqual(path1[v], path2[v])




