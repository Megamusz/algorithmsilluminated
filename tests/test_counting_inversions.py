import unittest
from algorithms import counting_inversions

class TestCountingInversions(unittest.TestCase):
    def test_sanity(self):
        _, inv_count = counting_inversions.count_inversions_sort_and_count([ 8,7,6,5,4,3,2,1 ])
        self.assertEqual(inv_count, 28)

    def test_inorder_array(self):
        _, inv_count = counting_inversions.count_inversions_sort_and_count([ 1,2,3,4,5,6,7,8 ])
        self.assertEqual(inv_count, 0)

    def test_small_array(self):
        with open('tests/problem3.5test.txt', 'r') as f:
             l = [int(l.strip()) for l in f.readlines()]
             _, inv_count = counting_inversions.count_inversions_sort_and_count(l)
             self.assertEqual(inv_count, counting_inversions.count_inversions_brute_force(l))
    
    def test_big_array(self):
        with open('tests/problem3.5.txt', 'r') as f:
            l = [int(l.strip()) for l in f.readlines()]
            _, inv_count = counting_inversions.count_inversions_sort_and_count(l)
            self.assertEqual(inv_count, 2407905288)

        
if __name__ == '__main__':
    unittest.main()