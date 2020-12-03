import unittest
from algorithms.huffman_encoding import huffman_encoding

class TestHuffman(unittest.TestCase):
    def test_case1(self):
        with open('tests/problem14.6test1.txt', 'r') as f:
            n = int(f.readline().strip())
            weights = []
            for i in range(n):
                weights.append(int(f.readline().strip()))
            
            self.assertEqual(min(huffman_encoding(weights)), 2)
            self.assertEqual(max(huffman_encoding(weights)), 5)

    def test_case2(self):
        with open('tests/problem14.6test2.txt', 'r') as f:
            n = int(f.readline().strip())
            weights = []
            for i in range(n):
                weights.append(int(f.readline().strip()))
            
            self.assertEqual(min(huffman_encoding(weights)), 3)
            self.assertEqual(max(huffman_encoding(weights)), 6)
    