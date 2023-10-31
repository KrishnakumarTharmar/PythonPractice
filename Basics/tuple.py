cars=("bmw","audi","tata","honda","bmw")
print(cars)
print(len(cars))
print(type(cars))
print(cars[2])
print(cars[1:4])
y=list(cars)
y[1]="toyota"
cars=tuple(y)
print(cars)
y.remove("bmw")
cars=tuple(y)
print(cars)
# del cars




tuple=("bmw",6,True,"apple")
print(tuple)