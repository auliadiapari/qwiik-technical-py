# test_triangle_logic.py
import unittest
from triangle_logic import triangle_type

class TestTriangleLogic(unittest.TestCase):

    def test_equilateral(self):
        result = triangle_type(5, 5, 5)
        self.assertEqual(result, "Equilateral")

    def test_isosceles(self):
        result = triangle_type(5, 5, 8)
        self.assertEqual(result, "Isosceles")

    def test_scalene(self):
        result = triangle_type(3, 4, 5)
        self.assertEqual(result, "Scalene")

if __name__ == '__main__':
    unittest.main()
