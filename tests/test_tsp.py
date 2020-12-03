import unittest
from algorithms.tsp_dp import tsp_dp, Graph

class TestTSP(unittest.TestCase):
    def test_case1(self):
        g = Graph(directed=False)
        g.from_file('tests/tsptest1.txt')
        self.assertEqual(tsp_dp(g._graph), 13)

    def test_case2(self):
        g = Graph(directed=False)
        g.from_file('tests/tsptest2.txt')
        self.assertEqual(tsp_dp(g._graph), 23)

    def test_case3(self):
        g = Graph(directed=False)
        g.from_file2('tests/tsptest3.txt')
        self.assertEqual(round(tsp_dp(g._graph), 2), 12.36)

    @unittest.skip("skip as this case is too slow")
    def test_challedge(self):
        g = Graph(directed=False)
        g.from_file2('tests/tspfile1.txt')
        print(tsp_dp(g._graph))