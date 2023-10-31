# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def multi(numbers):
    res=1
    for x in numbers:
        res*=x
    return res
print(multi((8, 2, 3, -1, 7)))