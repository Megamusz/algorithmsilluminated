import unittest
from algorithms.prim import prim_heap, Graph

class TestMST(unittest.TestCase):
    def test_case(self):
        g = Graph(directed= False)
        g.from_file('tests/problem15.9test.txt')
        self.assertEqual(prim_heap(g._graph), 14)
  