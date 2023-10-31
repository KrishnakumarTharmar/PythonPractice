department_data = {
    "Office": {
        "Kavin": 2010,
        "Ajay": 2015,
        "Naveen": 2005,
        "Maaran": 2018
    },
    "Plant": {
        "Srikanth": 2012,
        "Krishna": 2015,
        "Bala": 2009,
        "Karthick": 2014
    },
    "Site": {
        "Naresh": 2016,
        "Kumar": 2013,
        "Praveen": 2017,
        "Logesh": 2011
    }
}

senior_employees = {}
overall_senior = None
overall_senior_join_year = 9999

for department, employees in department_data.items():
    senior_employee = None
    senior_join_year = 9999

    for employee, join_year in employees.items():
        if join_year < senior_join_year:
            senior_employee = employee
            senior_join_year = join_year

    senior_employees[department] = senior_employee

    if senior_join_year < overall_senior_join_year:
        overall_senior = senior_employee
        overall_senior_join_year = senior_join_year

for department, senior_employee in senior_employees.items():
    print(f"The senior employee in {department} is {senior_employee}.")


print(f"The overall senior employee among all departments is {overall_senior}.")
