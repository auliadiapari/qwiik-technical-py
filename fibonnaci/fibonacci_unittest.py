



import unittest
from fibonacci_logic import generate_fibonacci

class TestFibonacciGeneration(unittest.TestCase):

    def test_generate_fibonacci(self):
        # Test with a few sample inputs
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8])

if __name__ == '__main__':
    unittest.main()