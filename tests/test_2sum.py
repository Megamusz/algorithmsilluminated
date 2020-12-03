import unittest
from algorithms.two_sum import two_sum

class Test2Sum(unittest.TestCase):
    def test_case(self):
        with open('tests/problem12.4test.txt', 'r') as f:
            A = []
            for line in f.readlines():
                A.append(int(line))
            
            self.assertEqual(two_sum(A, range(3, 11)), 8)

