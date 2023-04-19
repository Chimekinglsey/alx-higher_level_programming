#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 0, 0)
    r1.display()
	
    r1 = Rectangle(4, 5, 4, 2)
    r1.display()

    print("---")

    r2 = Rectangle(6, 6, 0, 3)
    r2.display()
