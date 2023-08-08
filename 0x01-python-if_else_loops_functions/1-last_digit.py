#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tempnumber = number

if number < 0:
    number = -(number)

last_digit = number % 10

if tempnumber < 0:
    number = tempnumber
    last_digit = -(last_digit)

if last_digit > 5:
    string = "and is greater than 5"
elif last_digit == 0:
    string = "and is 0"
elif last_digit < 6:
    string = "and is less than 6 and not 0"
print(f'Last digit of {number:d} is {last_digit:d} {string}')
