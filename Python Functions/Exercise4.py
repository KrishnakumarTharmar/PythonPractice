#Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name,salary=9000):
    print ("Name:",name, "Salary:",salary)
show_employee("Kavin",3000)
show_employee("Naveen",2000)
show_employee("Krishna")
show_employee("Rooban",4000)