
my_list = [1, 2, 3, 4, 5]

my_set = {3, 4, 5, 6, 7}

print("List:", my_list)
print("Set:", my_set)

my_list.append(6)
print("List after appending 6:", my_list)

my_list.remove(2)
print("List after removing 2:", my_list)

if 3 in my_list:
    print("3 is in the list")
if 8 not in my_set:
    print("8 is not in the set")

new_list = my_list + [7, 8, 9]
print("Joined list:", new_list)

union_set = my_set.union({7, 8, 9})
print("Union of sets:", union_set)

intersection_set = my_set.intersection({4, 5, 6, 10})
print("Intersection of sets:", intersection_set)

my_set.update({10, 11, 12})
print("Updated set:", my_set)
