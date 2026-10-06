from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    student_name : str
    student_phone : str 
    course : dict


