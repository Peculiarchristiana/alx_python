#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit of the number
number_str = str(number) 
last_digit = int(number_str[-1])
# Print the result based on the last digit
print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5: 
     print (f"and is greater than 5") 
if last_digit  == 0: 
     print (f"and is 0") 
if  0 < last_digit < 6 and last_digit !=0:
     print (f"and is less than 6 and not 0") 
