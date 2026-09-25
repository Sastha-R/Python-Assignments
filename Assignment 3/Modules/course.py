import csv
from pathlib import Path

COURSE_FILE : Path = Path("Data/Course_Details.csv")

def display_courses() -> None:
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







