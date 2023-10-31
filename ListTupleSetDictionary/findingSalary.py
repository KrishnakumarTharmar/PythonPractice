employee_salaries = {
    "Kavin": "20000",
    "Rooban": "15000",
    "Naveen": "30000",
    "Praveen": "40000",
    "Krishna": "10000"
}



def search_employee_salary(employee_name):
    salary = employee_salaries.get(employee_name)
    return salary


while True:
    employee_name = input(
        "Enter the employee name to search for (or 'exit' to quit): ")

    if employee_name.lower() == 'exit':
        break

    salary = search_employee_salary(employee_name)

    if salary:
        print("The salary of",employee_name, "is", salary)
    else:
        print(employee_name, "not found in the list of programs.")