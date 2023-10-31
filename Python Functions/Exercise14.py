# Write a Python function to check whether a number falls within a given range.

def checkRange(num):
    if num in range(0,10):
        print("Given number is less than 10")
    else:
        print("Given number is greater than 10")
checkRange(45)