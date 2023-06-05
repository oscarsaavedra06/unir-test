import unittest
from unittest.mock import patch
import pytest
import math
from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(0, 0))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(6, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertEqual(-4, self.calc.substract(-2, 2)) 

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertIsNot(1, self.calc.multiply(0, 0))
        self.assertIsNot(4, self.calc.multiply(-2, 2))

    def test_pot_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.power(8, 1))
        self.assertEqual(5, self.calc.power(5, 1))
        self.assertEqual(27, self.calc.power(3, 3))

    def test_sqr_method_returns_correct_result(self):
        self.assertEqual((1,2), self.calc.square(1,4))
        self.assertEqual((1,1.7724538509055159), self.calc.square(1,math.pi))

    def test_log_method_returns_correct_result(self):
        self.assertEqual((1,2), self.calc.log10(10,100))
        self.assertEqual((1.6989700043360188047862611052755,2.3010299956639811952137388947245), self.calc.log10(50,200))
    
    def test_log_method_fails_with_zero_and_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.log10 ,0,0)
        self.assertRaises(TypeError, self.calc.log10,-5,-2)

    def test_add_method_fails_with_nan_parameter(self):
            self.assertRaises(TypeError, self.calc.add, "2", 2)
            self.assertRaises(TypeError, self.calc.add, 2, "2")
            self.assertRaises(TypeError, self.calc.add, "2", "2")
            self.assertRaises(TypeError, self.calc.add, None, 2)
            self.assertRaises(TypeError, self.calc.add, 2, None)
            self.assertRaises(TypeError, self.calc.add, object(), 2)
            self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "1", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "4")
        self.assertRaises(TypeError, self.calc.substract, "2", "1")

    def test_mult_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 3)
        self.assertRaises(TypeError, self.calc.multiply, 3, "4")
        self.assertRaises(TypeError, self.calc.multiply, "1", "1")

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_pow_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "5", 3)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "1")
    
    def test_sqr_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square, "1", 1)
        self.assertRaises(TypeError, self.calc.square, 2, "5")
        self.assertRaises(TypeError, self.calc.square, "2", "2")
if __name__ == "__main__":  # pragma: no cover
    unittest.main()
