import unittest
from algorithms.randomized_selection import rselect


class TestRandomizedSelection(unittest.TestCase):
    def test_case1(self):
        with open('tests/problem6.5test1.txt', 'r') as f:
            l = [int(l.strip()) for l in f.readlines()]
            self.assertEqual(rselect(l, 0, 10, 4),
                5469)
 
    def test_case2(self):
        with open('tests/problem6.5test2.txt', 'r') as f:
            l = [int(l.strip()) for l in f.readlines()]
            self.assertEqual(rselect(l, 0, 100, 49),
                4715)
    
    @unittest.skip("skipping")
    def test_challenge(self):
        with open('tests/pi50.4.bin', 'rb') as f:
            l = []
            for i in range(1000000):
                v = 0
                for j in range(5):
                    byte = f.read(1)
                    assert(byte)
                    value = int.from_bytes(byte, 'big')

                    hi = (value >> 4) & 0xf
                    v = 10*v + hi
                    lo = (value) & 0xf
                    v = 10*v + lo
                    
                l.append(v)
        
            print(rselect(l, 0, len(l), len(l)/2 - 1))
