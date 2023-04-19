#!/usr/bin/python3
"""MODULE 1: CALCULATOR FOR TEST FILE"""


class Calc:
    """this is a calculator class for -, +, *, /, and % """
    def add(a, b):
        """sums a and b and returns the value"""
        return a + b

    def sub(a, b):
        """Gives the difference between a and b"""
        return a - b

	def mul(a, b):
        """returns the product of a and b"""
        return a * b

    def div(a, b):
        """returns the result of a/b if b is not zero"""
        if b == 0:
            raise ZeroDivisionError("b must not be '0'")
        return "{:.2f}".format(a/b)

    def mod(a, b):
        """returns remainder after integer division"""
        return a % b
