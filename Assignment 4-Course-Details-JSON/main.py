from Service.course_service import Course
from Service.enrollment_service import Enrollment
from Repository.Json_Repository import Json_Repository
import asyncio


json_repo = Json_Repository()
course_object = Course(json_repo)
enroll_object = Enrollment(json_repo)

async def main():
    while True:

        print("\n1. View Courses")
        print("2. Enroll Course")
        print("3. View Enrollments")
        print("4. Search Course")
        print("5. Cancel Enrollment")
        print("6. Search Enrollments")
        print("7. Sort Courses by Fees [Low to High]")
        print("8. Student Summary")
        print("9. Exit")

        try:
            choice : int = int(input("Enter your choice: "))

            match choice:
                case 1:
                    await course_object.display_courses()

                case 2:
                    await enroll_object.enroll_course()

                case 3:
                    await enroll_object.display_enrollments()

                case 4:
                    await course_object.search_course()

                case 5 :
                    await enroll_object.cancel_enrollment()

                case 6:
                       await enroll_object.filter_enrollments()

                case 7:
                    await course_object.sort_course()

                case 8:
                    await enroll_object.student_summary()

                case 9:
                    print("Exited")
                    break
                case _:
                    print("Invalid choice")

        except ValueError:
            print("Please enter a number.")

asyncio.run(main())