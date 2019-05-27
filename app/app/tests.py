from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that 2 numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_sub_number(self):
        """Test that 2 numbers are substracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
