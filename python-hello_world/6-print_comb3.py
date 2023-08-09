#!/usr/bin/python3
# Python program to print all 
# differnt combinations of two digits
for i in range(1, 10):
    for j in range(i + 1, 10):
        if i == 1:
            print("{:02d}".format(i), end=', ')
    if i != 9:
        print("{:02d}".format(i), end=', ')
    else:
        print("09")

             
