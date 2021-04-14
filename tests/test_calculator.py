import unittest
# from controllers.controller import *
from model.calculator import Calculator

class Test_calculator(unittest.TestCase):

    def setUp(self):
        self.number_1 = 3
        self.number_2 = 4
        self.number_3 = 8
        self.calculator = Calculator("normal_calculator")

    def test_calulator_adding_two_values(self):
        self.assertEqual(7,self.calculator.add_two_numbers(self.number_1, self.number_2))

    def test_calulator_multiply_two_values(self):
        self.assertEqual(12,self.calculator.multiply_two_numbers(self.number_1, self.number_2))

    def test_calulator_substraction_two_values(self):
        self.assertEqual(5,self.calculator.subtract_two_numbers(self.number_3, self.number_1))

    def test_calulator_division_two_values(self):
        self.assertEqual(2,self.calculator.divide_two_numbers(self.number_3, self.number_2))
