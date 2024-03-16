import pickle
from copy import deepcopy

from src.MyExceptions import ExistingStudent
from src.domain.Discipline import Discipline
from src.domain.Student import Student
from src.repository.GenerateEntries import generate_students

class StudentRepo:
    def __init__(self):
        self.__students = []
        self.undos = []
        self.redos = []
        self.pick_student_repository()

    def pick_student_repository(self):
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split("=")[1]
        if repo_type == "inmemory":
            self.__students = generate_students()
        elif repo_type == "textfiles":
            # now we have to read the filename
            file.readline()
            file.readline()
            filename = file.readline().strip().split("=")[1]    # filename = "disciplines.txt"
            self.load_text_data(filename)
        elif repo_type == "binaryfiles":
            # now we have to read the filename
            file.readline()
            file.readline()
            filename = file.readline().strip().split("=")[1]
            self.load_binary_data(filename)

    def load_binary_data(self, filename):
        file = open(filename, "rb+")
        try:
            aux = pickle.load(file)
        except EOFError:
            aux = []

        if len(aux) == 0:
            aux = generate_students()
        self.__students = aux
        file.close()

    def load_text_data(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            line = line.split(" ")
            self.__students.append(Student(int(line[0]), line[1]))
        if len(self.__students) == 0:
            self.__students = generate_students()
        file.close()

    def save_changes(self):
        # function that saves the changes made to the repository
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split("=")[1]
        file.readline()
        file.readline()
        if repo_type == "textfiles":
            filename = file.readline().strip().split("=")[1]
            self.save_text_changes(filename)
        elif repo_type == "binaryfiles":
            filename = file.readline().strip().split("=")[1]
            self.save_binary_changes(filename)

    def save_binary_changes(self, filename):
        file = open(filename, "wb+")
        pickle.dump(self.__students, file)
        file.close()

    def save_text_changes(self, filename):
        # function that saves the changes made to the repository
        file = open(filename, "w+")
        for student in self.__students:
            file.write(str(student.get_student_id()) + " " + student.get_name() + "\n")
        file.close()

    def undo(self):
        if len(self.undos) == 0:
            raise ValueError("No more undos!")
        self.redos.append(deepcopy(self.__students))
        self.__students = self.undos.pop()

    def redo(self):
        if len(self.redos) == 0:
            raise ValueError("No more redos!")
        self.undos.append(deepcopy(self.__students))
        self.__students = self.redos.pop()

    def add_student(self, student):
        for s in self.__students:
            if student.get_student_id() == s.get_student_id():
                raise ExistingStudent()
        self.__students.append(student)

    def remove(self, student):
        self.__students.remove(student)

    def get_all_students(self):
        return self.__students

    def remember_state(self):
        self.undos.append(deepcopy(self.__students))
        self.redos = []
