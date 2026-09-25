import csv
from pathlib import Path

COURSE_FILE: Path = Path("Data/Course_Details.csv")
ENROLL_FILE: Path = Path("Data/Enrollments.csv")

fields : list = ['enrollment_id','student_name','course_id','course_name','duration','fees',"staff","credits"]


def save_enrollment(student_name : str, course : dict) -> None:

    with open(ENROLL_FILE , "r" , newline="") as file:
        enroll = list(csv.DictReader(file))
        enrollment_id = len(enroll) + 1


    with open(ENROLL_FILE , "a" , newline="") as file:
        enroll = csv.DictWriter(file,fieldnames=fields)

        enroll.writerow({"enrollment_id": enrollment_id,
            "student_name": student_name,
            "course_id": course["id"],
            "course_name": course["coursename"],
            "duration": course["duration"],
            "fees": course["fees"],
            "staff": course["staff"],
            "credits": course["credits"]})


def enroll_course() -> None:
    try:
        student_name: str = input("Enter your name: ")
        course_id: int = int(input("Enter course ID: "))

        with open(COURSE_FILE, "r") as file:
            courses = csv.DictReader(file)
            found = False

            for course in courses:
                if int(course["id"]) == course_id:
                    print("\nSelected Course:")
                    print(f"Course Name : {course['coursename']}")
                    print(f"Duration    : {course['duration']} Months")
                    print(f"Fees        : {course['fees']}")
                    print(f"Staff       : {course['staff']}")
                    print(f"Credits     : {course['credits']}")
                    save_enrollment(student_name,course)
                    found = True
                    break

            if not found:
                print("\nno such course id")
    except ValueError:
        print("enter an numeric value for the id")

def display_enrollments() -> None:
      with open(ENROLL_FILE,"r") as file:
          enrollments = csv.DictReader(file)
          for enrollment in enrollments :
              print("Enrollment ID : ",enrollment["enrollment_id"]) 
              print("Student Name  : ",enrollment["student_name"],)
              print("Course ID     : ",enrollment["course_id"],)
              print("Course Name   : ",enrollment["course_name"],)
              print("Duration      : ",enrollment["duration"],)
              print("Fees          : ",enrollment["fees"],)
              print("Staff         : ",enrollment["staff"],)
              print("Credits       : ",enrollment["credits"],)
              print("-------------------------------------------------")



        