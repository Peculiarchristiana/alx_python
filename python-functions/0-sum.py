#!/usr/bin/env python3

# Function to add two integers
def add(a,b):
        result= a+b
        print (result)
        return (result)
def main():
    a=1
    b=2
        # calling the function with arguments a and b
    add(a,b)  
    add(100,-2)
    add(-100,-2)
    add(0,0) 

if __name__ == "__main__":
        main()