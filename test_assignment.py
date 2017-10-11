from assignment import Assignment
import pytest

def setup_assignment():
    assignment = Assignment("Hw", "Create a gradebook in python", "CS1", "01/01/2001") #replace "CS1" with classroom object
    return assignment

def test_setup():
    assignment = setup_assignment()
    assert assignment.name == "Hw"
    assert assignment.description == "Create a gradebook in python"
    assert assignment.classroom == "CS1"
    assert assignment.due_date == "01/01/2001"
