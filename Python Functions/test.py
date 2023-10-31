def test():
    print("This is my function")
test()

# ---------------

def test2(a, b):
    return a*b
print(test2(8,5))
print(test2(9,6))
print(test2(10,7))
print(test2(11,8))

# ---------------

def test3(food):
    for x in food:
        print(x)
fruits=["apple","banana","mango","orange"]
test3(fruits)