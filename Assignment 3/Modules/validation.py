def validate_name(name : str) -> bool:
    return name.replace(" ", "").isalpha()

def validate_course_id(course_id : int, course_count : int) -> bool:
    return 1 <= course_id <= course_count




