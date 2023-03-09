#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = abs(number) % 10
if num2 == 0:
    print("Last digit of {} is {} and is 0".format(number, num2))
elif num2 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num2))
elif num2 < 6:
    print("Last digit of {} is {} and is less than 6".format(number, num2))
