from Modules.course import *
from Modules.enrollment import *

while True:

    print("\n1. View Courses")
    print("2. Enroll Course")
    print("3. View Enrollments")
    print("4. Search Course")
    print("5. Exit")

    try:
        choice : int = int(input("Enter your choice: "))

        match choice:
            case 1:
                display_courses()

            case 2:
                enroll_course()

            case 3:
                display_enrollments()

            case 4:
                search_course()

            case 5:
                print("Exited")
                break

            case _:
                print("Invalid choice")

    except ValueError:
        print("Please enter a number.")