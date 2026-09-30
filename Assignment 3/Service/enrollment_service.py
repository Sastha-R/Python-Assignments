import csv
from pathlib import Path
from config import ENROLL_FILE,COURSE_FILE
from dataclasses import dataclass
from Utilities.validation import Validation
from Exception.custom_exceptions import EnrollmentNotFoundError
from Repository.Csv_Repository import Csv_Repository
# COURSE_FILE: Path = Path("Data/Course_Details.csv")
# ENROLL_FILE: Path = Path("Data/Enrollments.csv")

# fields : list = ['enrollment_id','student_name','course_id','course_name','duration','fees',"staff","credits"]


validation_obj = Validation() #validation object
csv_repository = Csv_Repository()

@dataclass
class Enrollment:
    fields : list

    def save_enrollment(self , student_name : str, student_phone : str ,course : dict) -> None:
        try:
            enrolls = csv_repository.read(ENROLL_FILE)
            enrollment_id = len(enrolls) + 1

            csv_repository.append(
                ENROLL_FILE,
                self.fields,
                {
                    "enrollment_id": enrollment_id,
                    "student_name": student_name,
                    "student_phone": student_phone,
                    "course_id": course["id"],
                    "course_name": course["coursename"],
                    "duration": course["duration"],
                    "fees": course["fees"],
                    "staff": course["staff"],
                    "credits": course["credits"]
                }
)

           
        except FileNotFoundError:
            print("Enrollments file not found.")
            return


    def enroll_course(self) -> None:
        try:

            student_name : str = input("Enter your name: ")
            if not validation_obj.validate_name(student_name):
                print("Invalid name. Enroll again")
                return


            student_phone : int = int(input("Enter your Phone Number : "))
            if not validation_obj.validation_phone(student_phone):
                print("invalid phone number")
                return 


            
            course_id : int = int(input("Enter course ID: "))

            courses = csv_repository.read(COURSE_FILE)

            course_count : int = len(courses)

            if not validation_obj.validate_course_id(course_id, course_count):
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
                    self.save_enrollment(student_name,student_phone,course)
                    break

            if not found_course:
                print("\nno such course id")
        except ValueError:
            print("value  must be a number")

    def display_enrollments(self) -> None:
        
        if not ENROLL_FILE.exists():
            print("No enrollments file found.")
            return
        
        enrollments: list = csv_repository.read(ENROLL_FILE)

        if not enrollments:
            print("No enrollments found.")
            return

        for enrollment in sorted(enrollments, key=lambda enrollment: int(enrollment["enrollment_id"])):
            
            print("Enrollment ID : ",enrollment["enrollment_id"]) 
            print("Student Name  : ",enrollment["student_name"],)
            print("Student Phone  : ",enrollment["student_phone"],)
            print("Course ID     : ",enrollment["course_id"],)
            print("Course Name   : ",enrollment["course_name"],)
            print("Duration      : ",enrollment["duration"],)
            print("Fees          : ",enrollment["fees"],)
            print("Staff         : ",enrollment["staff"],)
            print("Credits       : ",enrollment["credits"],)
            print("-------------------------------------------------")



    def cancel_enrollment(self) -> None :

        if not ENROLL_FILE.exists():
            print("no enroll file exist")
            return
        try:
            enrollment_id : int = int(input("enter the enrollment ID : "))
            enrollments: list = csv_repository.read(ENROLL_FILE)

            if not enrollments : 
                print("no enrollments found")
                return

            updated_enrollments = [enrollment for enrollment in enrollments if int(enrollment["enrollment_id"]) != enrollment_id]

            if len(updated_enrollments) == len(enrollments):
                raise EnrollmentNotFoundError("Enrollment not found.")

        
        except ValueError : 
            print("enter an valid number")

        except EnrollmentNotFoundError as error:
            print(error)

        else:
            csv_repository.write(ENROLL_FILE,self.fields,updated_enrollments)
            
            print("cancelled the enrollment")

