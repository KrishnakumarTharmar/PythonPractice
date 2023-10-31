import json

with open('D:\Python\Py Func\data.json', 'r') as json_file:
    data = json.load(json_file)

print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])
print("Email:", data["email"])
print("Interests:", ", ".join(data["interests"]))
print("Street Address:", data["address"]["street"])
print("ZIP Code:", data["address"]["zip"])
