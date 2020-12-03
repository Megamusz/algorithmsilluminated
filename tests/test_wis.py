import unittest
from algorithms.independent_set import independent_set

class TestWIS(unittest.TestCase):
    def test_case(self):
        with open('tests/problem16.6test.txt', 'r') as f:
            n = int(f.readline())
            l = []
            for i in range(n):
                l.append(int(f.readline()))
            self.assertEqual(sorted(independent_set(l)), [2, 4, 7, 10])
    
  