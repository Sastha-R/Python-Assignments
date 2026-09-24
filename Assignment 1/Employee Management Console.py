"""
Employee Management Console 
Maintain employee details using a collection. 

Menu: 
    1. Add Employee 
    2. View Employees 
    3. Search Employee 
    4. Find Highest Salary 
    5. Display Employees by Department 
    6. Exit 

Use: 
    List  
    Dictionary  
    Loop  
    match-case  
    Conditions  
    Searching  
    Comprehension  """






employees = []


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    employee = {
        "id": emp_id,
        "name": name,
        "salary": salary,
        "department": department
    }

    employees.append(employee)

    print("Employee added")


def view_employees():
    if not employees:
        print("No employees found.")
    else:
        print("\nEmployee Details")

        for employee in employees:
            print("ID         :", employee["id"])
            print("Name       :", employee["name"])
            print("Salary     :", employee["salary"])
            print("Department :", employee["department"])
            print()


def search_employee():
    search_name = input("Enter employee name to search: ")

    found = False

    for employee in employees:
        if employee["name"].lower() == search_name.lower():
            print("\nEmployee Found")
            print("ID         :", employee["id"])
            print("Name       :", employee["name"])
            print("Salary     :", employee["salary"])
            print("Department :", employee["department"])

            found = True
            break

    if not found:
        print("Employee not found.")


def highest_salary():

    if not employees:
        print("No employees found.")

    else:
        highest = max(employees, key=lambda employee: employee["salary"])

        

        print("\nEmployee with Highest Salary")
        print("ID         :", highest["id"])
        print("Name       :", highest["name"])
        print("Salary     :", highest["salary"])
        print("Department :", highest["department"])


def employees_by_department():
    department = input("Enter Department: ")

    department_employees = [employee for employee in employees if employee["department"].lower() == department.lower()]

    if department_employees:
        print("\nEmployees in", department)
    
        for employee in department_employees:
            print(employee["id"],"\n",employee["name"],"\n",employee["salary"])
    else:
        print("No employees found in this department.")


while True:

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Find Highest Salary")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_employee()

        case 2:
            view_employees()

        case 3:
            search_employee()

        case 4:
            highest_salary()

        case 5:
            employees_by_department()

        case 6:
            print("Exited")
            break

        case _:
            print("Invalid choice.")
