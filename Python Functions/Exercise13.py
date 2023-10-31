# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def findFactorial(num):
    if num==0:
        return 1
    else:
        res=num*findFactorial(num-1)
        return res
print(findFactorial(5))