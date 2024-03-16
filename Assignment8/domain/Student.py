class Student:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name

    def get_student_id(self):
        return self._student_id

    def to_string(self):
        return "Stud ID:" + str(self._student_id) + " Name: " + str(self._name)

    def get_name(self):
        return self._name

    def set_student_id(self, student_id):
        self._student_id = student_id

    def set_name(self, name):
        self._name = name
