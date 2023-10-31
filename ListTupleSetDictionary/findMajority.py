# def majority_element(arr):
#     count = 0
#     vehicle = None

#     for num in arr:
#         if count == 0:
#             vehicle = num
#         if num == vehicle:
#             count += 1
#         else:
#             count -= 1

#     return vehicle

# arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# majority = majority_element(arr)
# print("Majority Element:", majority)

def findingMajority(vehicles):
    count=0
    vehicle=None
    for x in vehicles:
        if count==0:
            vehicle=x
        if x==vehicle:
            count+=1
        else:
            count-=1
    return vehicle

vehicles=["Truck","Truck","JCB","Road Roller","JCB","Truck","Truck","JCB"]
result=findingMajority(vehicles)
print(result)
