import unittest
from algorithms import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_case1(self):
        with open('tests/problem5.6test1.txt', 'r') as f:
            l = [int(l.strip()) for l in f.readlines()]
            ls = sorted(l)
            self.assertNotEqual(l, ls)
            quick_sort.quick_sort(l, 0, len(l))
            self.assertEqual(l, ls)
    def test_case2(self):
        with open('tests/problem5.6test2.txt', 'r') as f:
            l = [int(l.strip()) for l in f.readlines()]
            ls = sorted(l)
            self.assertNotEqual(l, ls)
            quick_sort.quick_sort(l, 0, len(l))
            self.assertEqual(l, ls)

    def test_challenge(self):
        with open('tests/problem5.6.txt', 'r') as f:
            l = [int(l.strip()) for l in f.readlines()]
            ls = sorted(l)
            self.assertNotEqual(l, ls)
            quick_sort.quick_sort(l, 0, len(l))
            self.assertEqual(l, ls)
            
if __name__ == '__main__':
    unittest.main()