#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def calculation(a,b):
    c=a+b
    d=a-b
    return c,d
print(calculation(5,6))