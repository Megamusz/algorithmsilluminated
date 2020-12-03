import unittest
from algorithms import Karatsuba_multiplication

class TestKaratsubaMultiplication(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(Karatsuba_multiplication.karasuba_multiplication(99999, 9999),  999890001)

    def test_big_numbers(self):
        self.assertEqual(Karatsuba_multiplication.karasuba_multiplication(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627),
            3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627)
    def test_zero(self):
        self.assertEqual(Karatsuba_multiplication.karasuba_multiplication(1234, 0), 0)
        
if __name__ == '__main__':
    unittest.main()