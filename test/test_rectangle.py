import unittest
import sys
import os

# Dodaj ścieżkę do folderu `src`, aby Python mógł znaleźć moduły
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from rectangle import calculate_rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_area_calculation(self):
        self.assertEqual(calculate_rectangle_area(5, 4), 20)
        self.assertEqual(calculate_rectangle_area(3.5, 2), 7.0)
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 4)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, -4)
    
    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(0, 4)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, 0)

if __name__ == "__main__":
    unittest.main()