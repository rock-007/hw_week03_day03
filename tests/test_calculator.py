import unittest
from controllers.controller import *

class Test_calculator(unittest.TestCase):

    def setUp(self):
        self.number_1 = 3
        self.number_2 = 4

    def test_calulator_adding_two_values(self.number_1,self.number_2):
        self.assertEqual(7,)
