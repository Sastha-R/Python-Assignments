import csv
from pathlib import Path
from config import COURSE_FILE
from Exception.custom_exceptions import CourseNotFoundError
from Repository.Csv_Repository import Csv_Repository

# COURSE_FILE : Path = Path("Data/Course_Details.csv")


csv_repository = Csv_Repository()

class Course:
    def display_courses(self) -> None:
        try:
            courses = csv_repository.read(COURSE_FILE)

            for course in courses:
                print(f"Course ID   : {course['id']}\n"
                    f"Course Name : {course['coursename']}\n"
                    f"Duration    : {course['duration']} Months\n"
                    f"Fees        : {course['fees']}\n"
                    f"Staff       : {course['staff']}\n"
                    f"Credits     : {course['credits']}\n"
                    f"----------------------------------------")
        except FileNotFoundError:
            print("Course file not found.")


    def search_course(self) -> None:
        course_name: str = input("Enter course name: ")
        try:

            courses = csv_repository.read(COURSE_FILE)

            course_found = [course for course in courses if course_name.lower() in course["coursename"].lower()]


            if not course_found:
                raise CourseNotFoundError("Course not found.")

        except CourseNotFoundError as error:
            print(error)

        except FileNotFoundError:
            print("Course file not found.")

        else:
            for course in course_found:
                print("\nCourse Found:")
                print(f"Course ID   : {course['id']}")
                print(f"Course Name : {course['coursename']}")
                print(f"Duration    : {course['duration']} Months")
                print(f"Fees        : {course['fees']}")
                print(f"Staff       : {course['staff']}")
                print(f"Credits     : {course['credits']}")
                print("----------------------------------------")





