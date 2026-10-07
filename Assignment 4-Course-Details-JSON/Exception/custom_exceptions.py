class CourseNotFoundError(Exception):
    def __init__(self,course_name):
        self.course_name = course_name
        super().__init__(f"course {course_name} not found")


class EnrollmentNotFoundError(Exception):
    def __init__(self,enrollment_id):
        self.enrollment_id = enrollment_id
        super().__init__(f"Enrollment id {enrollment_id} is not found") 