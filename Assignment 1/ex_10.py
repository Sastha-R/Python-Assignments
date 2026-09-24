
students = []


def add_student():
    name = input("Enter Student Name: ")
    mark = float(input("Enter Mark: "))

    student = {
        "name": name,
        "mark": mark
    }

    students.append(student)

    print("Student added")


def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n Student Details")

        for student in students:
            print("Name :", student["name"])
            print("Mark :", student["mark"])
            print()


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found")
            print("Name :", student["name"])
            print("Mark :", student["mark"])

            found = True
            break

    if not found:
        print("Student not found.")


def calculate_average():
    if not students:
        print("No students found.")
    else:
        total = 0

        for student in students:
            total += student["mark"]

        average = total / len(students)

        print("Average Mark:", average)


def find_topper():
    if not students:
        print("No students found.")
    else:
        topper = students[0]

        for student in students:
            if student["mark"] > topper["mark"]:
                topper = student

        print("\nTopper Student")
        print("Name :", topper["name"])
        print("Mark :", topper["mark"])


def passed_students():
    passed_students = [student for student in students if student["mark"] >= 40]

    if passed_students:
        print("\n Passed Students")

        for student in passed_students:
            print(student["name"], "-", student["mark"])
    else:
        print("No students passed.")


while True:

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Passed Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_student()

        case 2:
            view_students()

        case 3:
            search_student()

        case 4:
            calculate_average()

        case 5:
            find_topper()

        case 6:
            passed_students()

        case 7:
            print("Exited")
            break

        case _:
            print("Invalid choice.")



