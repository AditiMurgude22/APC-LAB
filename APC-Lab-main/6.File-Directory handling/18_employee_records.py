# Employee record management

file = open("employees.txt", "w")

file.write("ID,Name,Department,Salary\n")
file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,45000\n")
file.write("103,Rahul,Finance,60000\n")

file.close()


def read_employees():
    file = open("employees.txt", "r")

    lines = file.readlines()

    file.close()

    employees = []

    for line in lines[1:]:
        emp_id, name, department, salary = line.strip().split(",")

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": int(salary)
        }

        employees.append(employee)

    return employees


def display_employees(employees):
    print("All Employees:")

    for employee in employees:
        print(employee)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x["salary"])

    print("\nHighest Paid Employee:")
    print(employee["name"], "-", employee["salary"])


def average_salary(employees):
    total = sum(employee["salary"] for employee in employees)

    average = total / len(employees)

    print("\nAverage Salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary, ":")

    for employee in employees:
        if employee["salary"] > salary:
            print(employee["name"], "-", employee["salary"])


employees = read_employees()

display_employees(employees)

highest_paid(employees)

average_salary(employees)

salary = int(input("\nEnter salary limit: "))

above_salary(employees, salary)