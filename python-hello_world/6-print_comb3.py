#!/usr/bin/python3
# Python program to print all 
# differnt combinations of two digits
for i in range(1,11):
    for j in range(i + 1, 99):
        print(f"{i:02}, {j:02}", end=', ')
    if i != 9:
        print(f"{i:02}, 10", end=', ')
    else:
        print("11, 10")


             
