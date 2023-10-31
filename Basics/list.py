fruits=["apple","banana","mango","orange","pineapple","banana","kiwi"] # It allows duplicates
print(fruits)
print(fruits[5])
print(fruits[-1])
print(fruits[1:5])
print(len(fruits))
print(type(fruits))
if "orange" in fruits:
    print("Yes orange is in the list")
fruits[5]="cherry"
print(fruits)
fruits.insert(2,"watermelon")
print(fruits)
fruits.append("grapes")
print(fruits)
fruits2=["plum","avocado","blueberry"]
fruits.extend(fruits2) # joins 2 lists
print(fruits)
fruits.remove("blueberry")
fruits.pop(3)
del fruits[1]
fruits.sort() # sorting
print(fruits)
fruits.sort(reverse=True) # reverse sorting
print(fruits)
fruits.reverse()
# fruits.clear()
# del fruits
print(fruits)




list1=["kavin",234,True,"apple"]
print(list1)