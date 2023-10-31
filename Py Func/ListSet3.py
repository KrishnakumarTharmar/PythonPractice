fruits=["apple","orange","banana"]
price={235,643,278}

con_price=list(price)
combine=dict(zip(fruits,con_price))

for fruit, cost in combine.items():
    print(fruit,"=",cost)