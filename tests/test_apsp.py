import unittest
from algorithms.floyd_warshall import floyd_warshall, Graph
from algorithms.johnson_apsp import johnson_apsp
import math

class TestAPSP(unittest.TestCase):
    def test_case1(self):
        g = Graph(directed = True)
        g.from_file('tests/problem18.8test1.txt')
        n = len(g._graph)

        A = floyd_warshall(g._graph)
        min_cost = math.inf

        negative_cycle = False
        for i in range(1, n + 1):
            if A[i][i] < 0:
                negative_cycle = True
                break

        if not negative_cycle:
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    min_cost = min(min_cost, A[i][j])
        self.assertEqual(min_cost,  -2)

    def test_case1_johnson(self):
        g = Graph(directed = True)
        g.from_file('tests/problem18.8test1.txt')
        n = len(g._graph)

        A = johnson_apsp(g._graph)
        min_cost = math.inf

        negative_cycle = False
        for i in range(1, n + 1):
            if A[i][i] < 0:
                negative_cycle = True
                break

        if not negative_cycle:
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    min_cost = min(min_cost, A[i][j])
        self.assertEqual(min_cost,  -2)

    def test_case2(self):
        g = Graph(directed = True)
        g.from_file('tests/problem18.8test2.txt')
        n = len(g._graph)

        A = floyd_warshall(g._graph)
        min_cost = math.inf

        negative_cycle = False
        for i in range(1, n + 1):
            if A[i][i] < 0:
                negative_cycle = True
                break

        if not negative_cycle:
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    min_cost = min(min_cost, A[i][j])
        self.assertEqual(negative_cycle,  True)

    def test_case2_johnson(self):
        g = Graph(directed = True)
        g.from_file('tests/problem18.8test2.txt')
        n = len(g._graph)

        A = johnson_apsp(g._graph)   
        negative_cycle = not A
        
        self.assertEqual(negative_cycle,  True)
        