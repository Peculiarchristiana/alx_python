#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = repr (number) 
last_digit_string = number_string[-1]
last_digit = int(last_digit_string)
if last_digit (number) > 5: 
     print (f"Last digit of (number) is last_digit and is greater than 5") 
if last_digit (number) == 0: 
     print (f"Last digit of (number) is last_digit and is 0") 
if last_digit (number) < 6  and last_digit (number) != 0: 
     print (f"Last digit of (number) is last_digit and is less than 6 and not 0") 
