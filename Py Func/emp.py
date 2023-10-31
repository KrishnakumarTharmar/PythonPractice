class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Name:",self.name)
        print("Position:",self.position)
        print("Salary: ${:.2f}".format(self.salary))

employee1 = Employee(101, "Kavin", "Manager", 60000)
employee2 = Employee(102, "Krishnakumar", "Engineer", 50000)

print("Employee 1 Information:")
employee1.display_employee_info()

print("\nEmployee 2 Information:")
employee2.display_employee_info()
