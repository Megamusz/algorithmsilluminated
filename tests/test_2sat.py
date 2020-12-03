import unittest
from algorithms.papadimitriou_2sat import papadimitriou_2sat


class TestPapadimitriou(unittest.TestCase):
    def test_case1(self):
        n = 8
        x = [True for i in range(n+1)]
        A = [(8, -8), (-3, 4), (2, -8), (3, 3), (2, 6), (-2, -6), (1, 6), (4, 8)]
        
        self.assertEqual(papadimitriou_2sat(A, n), True)

    def test_case2(self):
        n = 8
        x = [True for i in range(n+1)]
        A = [(7, -1), (2, 5), (-5, 4), (-2, 5), (-7, -7), (-1, -7), (-3, 2), (-5, 1)]
        
        
        self.assertEqual(papadimitriou_2sat(A, n), False)