"""
Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.
"""

"""
Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. 
Your tests should cover various scenarios to ensure the class functions correctly.
"""
import unittest
from simple_calculator import SimpleCalculator # custom module

calc = SimpleCalculator()
#test class
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        result = calc.add(2, 5)
        self.assertEqual(result, 7)
        self.assertEqual(self.calc.add(3, -1), 2)

    def test_subtraction(self):
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multiply(self):
        result = calc.multiply(2, 5)
        self.assertEqual(result, 10)
        self.assertEqual(calc.multiply(4, -7), -28)
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_divide(self):
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)
        self.assertEqual(self.calc.divide(4, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(4, 0)
             
if __name__ == "__main__":
    unittest.main()