"""Module docstring. Write something clever."""
import logging

_LOGGER = logging.getLogger(__name__)


class Aclass:
    """Class docstring. Write something clever.

    Maybe something about inputs and outputs.
    """

    def __init__(self, first_variable, second_variable=2):
        self.first_variable = first_variable
        self.second_variable = second_variable
        _LOGGER.debug("init a class")

    def add(self):
        """Add first and second variable."""
        _LOGGER.debug("add first and second variable")
        return self.first_variable + self.second_variable

    def set_a(self, first_variable):
        """Set first variable."""
        _LOGGER.debug("set first variable")
        self.first_variable = first_variable

    def set_b(self, second_variable):
        """Set second variable."""
        _LOGGER.debug("set second variable")