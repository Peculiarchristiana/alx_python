#!/usr/bin/env python3
#import the '0-sum' module
add = __import__('0-sum').add
a = 1
b = 2
#functions to add two integers
def add(a,b):
    #printing results
    print(add(a,b))
    print(add(98, 0))
    print(add(100, -2))
    print(add(0, 0))
add(a,b)
# and return the sum of those two integer