import unittest
from algorithms.knapsack import knapsack_optimized

class TestKnapsack(unittest.TestCase):
    def test_case(self):
        with open('tests/problem16.7test.txt', 'r') as f:
            W, n = f.readline().strip().split()
            items = []
            for i in range(int(n)):
                v, w = f.readline().strip().split()
                items.append((int(v), int(w)))
            
            self.assertEqual(knapsack_optimized(items, int(W)), 2493893)
    
    