import unittest
from algorithms.prim_mst import prim_heap, Graph
from algorithms.kruskal_mst import kruskal_mst

class TestMST(unittest.TestCase):
    def test_case_prim(self):
        g = Graph(directed= False)
        g.from_file('tests/problem15.9test.txt')
        self.assertEqual(prim_heap(g._graph), 14)
    
    def test_case_kruskal(self):
        with open('tests/problem15.9test.txt', 'r') as f:
            n, m = f.readline().strip().split()
            G = []
            for _ in range(int(m)):
                u, v, w = f.readline().strip().split()
                G.append(((int(u), int(v)), int(w)))
            T = kruskal_mst(G, int(n))
            cost = 0
            for e in T:
                cost += e[1]

            self.assertEqual(cost, 14)

    def test_case_challenge(self):
        g = Graph(directed= False)
        g.from_file('tests/problem15.9.txt')
        cost_prim = prim_heap(g._graph)
        
        with open('tests/problem15.9.txt', 'r') as f:
            n, m = f.readline().strip().split()
            G = []
            for _ in range(int(m)):
                u, v, w = f.readline().strip().split()
                G.append(((int(u), int(v)), int(w)))
            T = kruskal_mst(G, int(n))
            cost_kruskal = 0
            for e in T:
                cost_kruskal += e[1]
        self.assertEqual(cost_prim, cost_kruskal)