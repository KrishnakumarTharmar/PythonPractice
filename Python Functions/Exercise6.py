# Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself again and again.

def my_function(num):
    if num:
        return num + my_function(num-1)
    else:
        return 0
result=my_function(20)
print(result)