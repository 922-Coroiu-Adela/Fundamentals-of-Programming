# making my own class of exceptions

class ExistenceStudent(Exception):
    def __init__(self):
        self.message = f"The student doesn't exist!"

class ExistingStudent(Exception):
    def __init__(self):
        self.message = "The student is already existing!"

class ExistenceDiscipline(Exception):
    def __init__(self):
        self.message = f"The discipline doesn't exist!"

class ExistingDiscipline(Exception):
    def __init__(self):
        self.message = "The discipline is already existing!"

class GradeException(Exception):
    def __init__(self):
        self.message = "The grade must be between 1 and 10!"
