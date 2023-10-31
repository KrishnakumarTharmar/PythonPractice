class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self) -> str:
        return self.name
    def greet(self):
        print("hello",self.name)
t=test("krishna",22)
print(t)
t.greet()