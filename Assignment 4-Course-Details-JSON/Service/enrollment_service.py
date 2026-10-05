from pathlib import Path
from config import ENROLL_FILE,COURSE_FILE
from dataclasses import dataclass
from Utilities.validation import Validation
from Exception.custom_exceptions import EnrollmentNotFoundError
from Repository.Json_Repository import Json_Repository



validation_obj = Validation() #validation object
# csv_repository = Csv_Repository()

@dataclass
class Enrollment:
    json_repository : Json_Repository

    # def __init__(self, csv_repo):
    #     self.csv_repo = csv_repo


    def save_enrollment(self ,student_id: int, student_name : str, student_phone : str ,course : dict) -> None:
        try:
            enrolls = self.json_repository.read(ENROLL_FILE)
            enrollment_id : int  = len(enrolls) + 1

            self.json_repository.append(
                ENROLL_FILE,
                {
                    "enrollment_id": enrollment_id,
                    "student_id": student_id,
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

            student_id: int = int(input("Enter your Student ID: "))
            
            student_name : str = input("Enter your name: ")
            if not validation_obj.validate_name(student_name):
                print("Invalid name. Enroll again")
                return


            student_phone : int = int(input("Enter your Phone Number : "))
            if not validation_obj.validation_phone(student_phone):
                print("invalid phone number")
                return 


            
            course_id : int = int(input("Enter course ID: "))

            courses = self.json_repository.read(COURSE_FILE)

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
                self.save_enrollment(student_id,student_name,student_phone,course)
                break

            if not found_course:
                print("\nno such course id")
        except ValueError:
            print("value  must be a number thranish")

    def display_enrollments(self) -> None:
        
        if not ENROLL_FILE.exists():
            print("No enrollments file found.")
            return
        
        enrollments: list = self.json_repository.read(ENROLL_FILE)

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
            enrollments: list = self.json_repository.read(ENROLL_FILE)

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
            self.json_repository.write(ENROLL_FILE,updated_enrollments)
            
            print("cancelled the enrollment") 


   

    def filter_enrollments(self) -> None:

        try:
            enrollment_id: int = int(input("Enter Enrollment ID: "))

            enrollments = self.json_repository.read(ENROLL_FILE)

            filtered_enrollments = list(
                filter(
                    lambda enrollment: int(enrollment["enrollment_id"]) == enrollment_id,
                    enrollments
                )
            )

            if not filtered_enrollments:
                print("No enrollments found.")
                return

            for enrollment in filtered_enrollments:
                print("\nEnrollment ID  :", enrollment["enrollment_id"])
                print("Student Name     :", enrollment["student_name"])
                print("Course Name      :", enrollment["course_name"])

        except ValueError:
            print("Enter a valid number.")


    


    def student_summary(self) -> None:

        enrollments = self.json_repository.read(ENROLL_FILE)

        student_ids = sorted(set(map( lambda enrollment: enrollment["student_id"] , enrollments)))

        for student_id in student_ids:
            student_enrollments = list(
                filter(
                    lambda enrollment : enrollment["student_id"] == student_id,
                    enrollments
                )
            )

            total_fees =sum(
                map(
                    lambda enrollment: int(enrollment["fees"]),
                    student_enrollments
                )
            )

            total_duration = sum(
                map(
                    lambda enrollment: int(enrollment["duration"]),
                    student_enrollments
                )
            )
            total_credits =sum(
                map(
                lambda enrollment: int(enrollment["credits"]),
                    student_enrollments
                )
            )

            print("\nStudent ID   :", student_id)
            print("Student Name   :", student_enrollments[0]["student_name"])
            print("Total Fees     :", total_fees)
            print("Total Duration :", total_duration, "Months")
            print("Total Credits  :", total_credits)
            print("--------------------------------")


