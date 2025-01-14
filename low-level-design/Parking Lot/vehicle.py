"""This module defines a Vehicle class for representing vehicle attributes and behaviors."""

from type import Type

class Vehicle(Type):
    """A Vehicle Class"""
    def __init__(self, registration_no: str, color: str, vechile_type):
        super().__init__(vechile_type)
        self._registration_no = registration_no
        self._color = color

    def get_registration_number(self):
        """Returns the registration number"""
        return self._registration_no

    def set_registration_number(self, registration_no):
        """Sets the registration number"""
        self._registration_no = registration_no

    def get_color(self):
        """Returns the color"""
        return self._color

    def set_color(self, color):
        """Sets the color"""
        self._color = color
    