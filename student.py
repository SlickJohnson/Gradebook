class Student(object):

    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        self.GPA = None
        self.assignments = {}

    def add_assignment(self, assignment):
        self.assignments = {assignment: None}

    def get_GPA(self):
        update_GPA()
        return self.GPA

    def update_GPA(self):
        
