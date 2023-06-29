"""Module docstring. Write something clever."""
from unittest import TestCase

from src.module1 import Aclass


class TestAclass(TestCase):
    """Class docstring. Write something clever.

    Maybe something about inputs and outputs.
    """

    def setUp(self):
        """Set up for tests."""
        self.aclass = Aclass(first_variable=0)

    def tearDown(self):
        """Tear down after tests."""
        return None

    def test_set_first_variable_read_back_equal(self):
        """A test."""
        expected = 2
        self.aclass.set_a(first_variable=expected)
        result = self.aclass.first_variable
        self.assertEqual(first=expected, second=result)

    def test_set_second_variable_read_back_equal(self):
        """A test."""
        expected = 2
        self.aclass.set_b(second_variable=expected)
        result = self.aclass.second_variable
        self.assertEqual(first=expected, second=result)

    def test_add_returns_expected(self):
        """A test."""
        expected = 2
        result = self.aclass.add()
        self.assertEqual(first=expected, second=result)
