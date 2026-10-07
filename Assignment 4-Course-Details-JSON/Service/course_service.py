import csv
from pathlib import Path
from config import COURSE_FILE
from Exception.custom_exceptions import CourseNotFoundError
from Repository.Json_Repository import Json_Repository
from dataclasses import dataclass
from pydantic import BaseModel, ConfigDict


# COURSE_FILE : Path = Path("Data/Course_Details.csv")


class Course(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    json_repository : Json_Repository

    async def display_courses(self) -> None:
        try:
            courses = await self.json_repository.read(COURSE_FILE)

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


    async def search_course(self) -> None:
        course_name: str = input("Enter course name: ")
        try:

            courses = await self.json_repository.read(COURSE_FILE)

            course_found = [course for course in courses if course_name.lower() in course["coursename"].lower()]


            if not course_found:
                raise CourseNotFoundError(course_name)

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


    async def sort_course(self) -> None:

            courses = await self.json_repository.read(COURSE_FILE)

            sorted_courses = sorted( courses, key=lambda course: course["fees"])

            for course in sorted_courses:
                print(f"Course ID   : {course['id']}\n"
                      f"Course Name : {course['coursename']}\n"
                      f"Duration    : {course['duration']} Months\n"
                      f"Fees        : {course['fees']}\n"
                      f"Staff       : {course['staff']}\n"
                      f"Credits     : {course['credits']}\n"
                      f"----------------------------------------")



