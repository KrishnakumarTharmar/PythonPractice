#Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum(num):
    res=0
    for x in num:
        res+=x
    return res
print(sum((8, 2, 3, 0, 7)))
