import unittest
from functions.PrimeFunc import TestClass

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.prime = TestClass()

    def test_prime_1(self):
        self.assertEqual(self.prime.isPrime(11), 1)
    def test_prime_2(self):
        self.assertEqual(self.prime.isPrime(0), -1)
    def test_prime_3(self):
        self.assertEqual(self.prime.isPrime(-234), -1)
    def test_prime_4(self):
        self.assertEqual(self.prime.isPrime(987654323), 1)
    def test_prime_5(self):
        self.assertEqual(self.prime.isPrime(20), 0)


if __name__ == '__main__':
    unittest.main()
