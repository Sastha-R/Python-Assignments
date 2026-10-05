import pytest


@pytest.fixture
def sample_courses():
    return [
        {"id": "1", "coursename": "Python Basics"},
        {"id": "2", "coursename": "Data Science"},
    ]


def test_find_matching_course(sample_courses):
    search_name = "python"

    matches = [course for course in sample_courses if search_name.lower() in course["coursename"].lower()]

    assert len(matches) == 1
    assert matches[0]["coursename"] == "Python Basics"


def test_no_matching_course(sample_courses):
    search_name = "biology"

    matches = [ course for course in sample_courses if search_name.lower() in course["coursename"].lower()]

    assert matches == []