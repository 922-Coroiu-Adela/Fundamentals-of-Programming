class Discipline:
    def __init__(self, discipline_id, name):
        self._discipline_id = discipline_id
        self._name = name

    def get_discipline_id(self):
        return self._discipline_id

    def to_string(self):
        return "Discipl ID: " + str(self._discipline_id) + " Name: " + str(self._name)

    def get_name(self):
        return self._name

    def set_discipline_id(self, discipline_id):
        self._discipline_id = discipline_id

    def set_name(self, name):
        self._name = name