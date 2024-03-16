class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        self._discipline_id = discipline_id
        self._student_id = student_id
        self._grade_value = grade_value

    def get_discipline_id(self):
        return self._discipline_id

    def get_student_id(self):
        return self._student_id

    def to_string(self):
        return "Discipl ID:" + str(self._discipline_id) + " Stud ID: " + str(self._student_id) + " Grade: " + str(self._grade_value)

    def get_grade_value(self):
        return self._grade_value

    def set_discipline_id(self, discipline_id):
        self._discipline_id = discipline_id

    def set_student_id(self, student_id):
        self._student_id = student_id

    def set_grade_value(self, grade_value):
        self._grade_value = grade_value