from Service.course_service import Course
from Service.enrollment_service import Enrollment


fields : list = ['enrollment_id','student_name','student_phone','course_id','course_name','duration','fees',"staff","credits"]


course_object = Course()
enroll_object = Enrollment(fields)


while True:

    print("\n1. View Courses")
    print("2. Enroll Course")
    print("3. View Enrollments")
    print("4. Search Course")
    print("5. Cancel Enrollment")
    print("6. Exit")

    try:
        choice : int = int(input("Enter your choice: "))

        match choice:
            case 1:
                course_object.display_courses()

            case 2:
                enroll_object.enroll_course()

            case 3:
                enroll_object.display_enrollments()

            case 4:
                course_object.search_course()

            case 5 :
                enroll_object.cancel_enrollment()

            case 6:
                print("Exited")
                break

            case _:
                print("Invalid choice")

    except ValueError:
        print("Please enter a number.")