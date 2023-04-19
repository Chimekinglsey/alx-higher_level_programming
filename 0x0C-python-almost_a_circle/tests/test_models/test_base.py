#!/usr/bin/python3
"""MODULE 0: TEST FILE FOR BASE CLASS"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """we are testing all our base class to be sure it instantiates"""
    def test_intantiation(self):
        """this will test whether instantiation of base is proper"""
        b = Base()
        b2 = Base()
        self.assertEqual(b.id, b2.id -1)

    def test_initialization(self):
        """testing if id changes when initialized from base"""
        b3 = Base(50)
        self.assertEqual(b3.id, 50)
        b3.id = 12
        self.assertEqual(b3.id, 12)

    def test_flow(self):
        """Checking if every object of Base retains value after"""
        new = Base()
        self.assertEqual(new.id, 1)
        
if __name__ == "__main__":
    unittest()
