import unittest
# from controllers.controller import *
from modules.calculator import Calculator

class Test_calculator(unittest.TestCase):

    def setUp(self):
        self.number_1 = 3
        self.number_2 = 4
        self.calculator = Calculator("normal_calculator")

    def test_calulator_adding_two_values(self):
        self.assertEqual(7,self.calculator.add_two_numbers(self.number_1, self.number_2))
