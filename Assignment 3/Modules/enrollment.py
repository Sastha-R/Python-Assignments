import csv
from pathlib import Path
from Modules.validation import *
from Modules.config import ENROLL_FILE,COURSE_FILE

# COURSE_FILE: Path = Path("Data/Course_Details.csv")
# ENROLL_FILE: Path = Path("Data/Enrollments.csv")

fields : list = ['enrollment_id','student_name','course_id','course_name','duration','fees',"staff","credits"]


def save_enrollment(student_name : str, course : dict) -> None:
    try:
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
    except FileNotFoundError:
        print("Enrollments file not found.")
        return


def enroll_course() -> None:
    try:
        student_name : str = input("Enter your name: ")
        if not validate_name(student_name):
            print("Invalid name. Enroll again")
            return
        course_id : int = int(input("Enter course ID: "))

        with open(COURSE_FILE, "r") as file:
            courses = list(csv.DictReader(file))

            course_count : int = len(courses)

            if not validate_course_id(course_id, course_count):
                print("Invalid course ID. ID should be between 1 and ",course_count)
                return


            found_course = [course for course in courses if int(course["id"]) == course_id]

            for course in found_course:
                
                    print("\nSelected Course:")
                    print(f"Course Name : {course['coursename']}")
                    print(f"Duration    : {course['duration']} Months")
                    print(f"Fees        : {course['fees']}")
                    print(f"Staff       : {course['staff']}")
                    print(f"Credits     : {course['credits']}")
                    save_enrollment(student_name,course)
                    break

            if not found_course:
                print("\nno such course id")
    except ValueError:
        print("Course ID must be a number")

def display_enrollments() -> None:
      
      if not ENROLL_FILE.exists():
        print("No enrollments file found.")
        return
      
      with open(ENROLL_FILE,"r") as file:
          enrollments = list(csv.DictReader(file))
          if not enrollments:
            print("No enrollments found.")
            return

          for enrollment in sorted(enrollments, key=lambda enrollment: int(enrollment["enrollment_id"])):
              
              print("Enrollment ID : ",enrollment["enrollment_id"]) 
              print("Student Name  : ",enrollment["student_name"],)
              print("Course ID     : ",enrollment["course_id"],)
              print("Course Name   : ",enrollment["course_name"],)
              print("Duration      : ",enrollment["duration"],)
              print("Fees          : ",enrollment["fees"],)
              print("Staff         : ",enrollment["staff"],)
              print("Credits       : ",enrollment["credits"],)
              print("-------------------------------------------------")



        