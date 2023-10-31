names={"kavin","krishna","rooban","navin","kavin"} # unordered, unchangeable and doesn't allow duplicates
print(names)
print(len(names))
print(type(names))
for x in names:
    print(x)
names.add("ajay")
names.add("praveen")
print(names)
names2={"akash","dinesh","logesh"}
names.update(names2)
print(names)
names.remove("akash")
print(names)
y=names.pop() # remove random item
print(y,names)
# names.clear()
# del names
names2={"karthick","sathish","santhosh"}
res=names.union(names2) # use union() or update()
print(res)


set={"kavin", 18, True, "apple"}
print(set)