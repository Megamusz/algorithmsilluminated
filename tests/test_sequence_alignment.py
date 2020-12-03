import unittest
from algorithms.sequence_alignment import sequence_alignment

class TestMST(unittest.TestCase):
    def test_case(self):
        with open('tests/problem17.8nw.txt', 'r') as f:
            n, m = f.readline().strip().split()
            penalty_gap, penalty_mismatch = f.readline().strip().split()

            X = f.readline().strip()
            Y = f.readline().strip()

            assert(len(X) == int(n))
            assert(len(Y) == int(m))

            self.assertEqual(sequence_alignment(X, Y, int(penalty_gap), int(penalty_mismatch)), 224)