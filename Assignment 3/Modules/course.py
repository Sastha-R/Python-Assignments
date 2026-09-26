import csv
from pathlib import Path
from Modules.config import COURSE_FILE

# COURSE_FILE : Path = Path("Data/Course_Details.csv")

def display_courses() -> None:
    try:
        with open(COURSE_FILE,"r") as file:
            courses = csv.DictReader(file)

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


def search_course() -> None:
    course_name: str = input("Enter course name: ")
    try:

        with open(COURSE_FILE, "r") as file:
            courses = csv.DictReader(file)

            found = False

            for course in courses:
                if course_name.lower() in course["coursename"].lower():
                    print("\nCourse Found:")
                    print(f"Course ID   : {course['id']}")
                    print(f"Course Name : {course['coursename']}")
                    print(f"Duration    : {course['duration']} Months")
                    print(f"Fees        : {course['fees']}")
                    print(f"Staff       : {course['staff']}")
                    print(f"Credits     : {course['credits']}")
                    print("----------------------------------------")

                    found = True

            if not found:
                print("Course not found.")
    except FileNotFoundError:
        print("Course file not found.")







