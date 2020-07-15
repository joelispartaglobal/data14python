from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):
    calc = SimpleCalc()

    # Lets write some tests
    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(-4, -10), -14)
        self.assertEqual(self.calc.add(-3, 5), 2)
        self.assertEqual(self.calc.add(7, -1), 6)
        self.assertIsNone(self.calc.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(-3, -8), 5)
        self.assertEqual(self.calc.subtract(2, -2), 4)
        self.assertEqual(self.calc.subtract(-20, 2), -22)
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertIsNone(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(-6, -1), 6)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(1, -4), -4)
        self.assertIsNone(self.calc.multiply(0, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(3, -2), -1.5)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(-5, 5), -1)
        self.assertIsNone(self.calc.divide(0, 5), 0)
        # self.assertEqual(self.calc.divide(1, 0), "Undefined")
        # self.assertEqual(self.calc.divide(0, 0), "Undefined")
