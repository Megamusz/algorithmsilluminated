import unittest
from algorithms.optimal_bst import optimal_bst

class TestOptBST(unittest.TestCase):
    def test_case(self):
        with open('tests/problem17.8optbst.txt', 'r') as f:
            n = int(f.readline().strip())
            W = [int(x) for x in f.readline().strip().split(',')]
            assert(len(W) == n)
            self.assertEqual(optimal_bst(W), 2780)