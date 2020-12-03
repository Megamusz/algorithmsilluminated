import unittest
from algorithms.graph import Graph
from algorithms.kosaraju_scc import kosaraju_scc

class TestSCC(unittest.TestCase):
    def test_case1(self):
        g = Graph(directed = True)
        g.from_file('tests/problem8.10test1.txt')
        self.assertEqual(kosaraju_scc(g._graph), [3, 3, 3, 0, 0])

    def test_case2(self):
        g = Graph(directed = True)
        g.from_file('tests/problem8.10test2.txt')
        self.assertEqual(kosaraju_scc(g._graph), [3, 3, 2, 0, 0])

    def test_case3(self):
        g = Graph(directed = True)
        g.from_file('tests/problem8.10test3.txt')
        self.assertEqual(kosaraju_scc(g._graph), [3, 3, 1, 1, 0])
    
    def test_case4(self):
        g = Graph(directed = True)
        g.from_file('tests/problem8.10test4.txt')
        self.assertEqual(kosaraju_scc(g._graph), [7, 1, 0, 0, 0])

    def test_case5(self):
        g = Graph(directed = True)
        g.from_file('tests/problem8.10test5.txt')
        self.assertEqual(kosaraju_scc(g._graph), [6, 3, 2, 1, 0])