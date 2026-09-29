class Validation:
    def validate_name(self , name : str) -> bool:
        return name.replace(" ", "").isalpha()

    def validate_course_id(self , course_id : int, course_count : int) -> bool:
        return 1 <= course_id <= course_count

    def validation_phone(self, phone : int) -> bool:
         return len(str(phone)) == 10


