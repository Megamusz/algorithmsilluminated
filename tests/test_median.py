import unittest
from algorithms.median_maintenance import median_maintenance

class TestMedian(unittest.TestCase):
    def test_case(self):
        with open('tests/problem11.3test.txt', 'r') as f:
            l = f.readlines()
            l = [int(i) for i in l]
            self.assertEqual(median_maintenance(l), 9335)

