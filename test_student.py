import pytest

def setup_student():
    student = Student("Willie Johnson", 1)
    return student

def test_setup():
    student = setup_student()
    assert student.name == "Willie Johnson"
    assert student.student_ID == 1
    assert student.grade_in_class == None
    assert len(student.assignments) == 0

test_setup()
