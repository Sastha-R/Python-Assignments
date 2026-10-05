from Utilities.validation import Validation

validation = Validation()


def test_valid_name():
    assert validation.validate_name("Walter White") == True

def test_invalid_name():
    assert validation.validate_name("Walter123") == False

def test_valid_course_id():
    assert validation.validate_course_id(2, 10) == True


def test_invalid_course_id():
    assert validation.validate_course_id(15, 10) == False

def test_valid_phone():
    assert validation.validation_phone(9876543210) == True

def test_invalid_phone():
    assert validation.validation_phone(12345) == False