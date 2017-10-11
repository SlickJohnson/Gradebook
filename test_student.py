from student import Student
from assignment import Assignment

import pytest

def setup_student():
    student = Student("Willie Johnson", 1)
    return student

def setup_assignment():
    assignment = Assignment("Hw", "Create a gradebook in python", "CS1", "01/01/2001")
    return assignment

def test_setup():
    student = setup_student()

    assert student.name == "Willie Johnson"
    assert student.student_ID == 1
    assert student.GPA == None
    assert len(student.assignments) == 0

def test_student_add_assignment():
    student = setup_student()
    assignment = setup_assignment()
    student.add_assignment(assignment)

    assert len(student.assignments) == 1
    assert student.assignments[assignment] == None

    student.assignments[assignment] = 100
    assert student.assignments[assignment] == 100
