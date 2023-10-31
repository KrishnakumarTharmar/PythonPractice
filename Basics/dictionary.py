dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 3030, # duplicates not allowed
  "colors": ["green","blue","red","yellow"]
}
print(dict)
print(len(dict))
print(type(dict))
print(dict["model"])
x=dict.keys()
print(x)
y=dict.values()
print(y)
z=dict.items()
print(z)
dict.update({"year":4040})
print(dict)
dict.pop("colors")
print(dict)
dict.popitem() # removes last item
print(dict)
# dict.clear()
# del dict

mydict=dict.copy()
print(mydict)