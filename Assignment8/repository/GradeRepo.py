import pickle
from copy import deepcopy

from src.MyExceptions import GradeException
from src.domain.Grade import Grade
from src.repository.GenerateEntries import generate_grades

class GradeRepo:
    def __init__(self):
        self.__grades = []
        self.undos = []
        self.redos = []
        self.pick_grade_repository()

    def pick_grade_repository(self):
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split("=")[1]
        if repo_type == "inmemory":
            self.__grades = generate_grades()
        elif repo_type == "textfiles":
            # now we have to read the filename
            file.readline()
            filename = file.readline().strip().split("=")[1]
            self.load_text_data(filename)
        elif repo_type == "binaryfiles":
            # now we have to read the filename
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
            aux = generate_grades()
        self.__grades = aux
        file.close()

    def load_text_data(self, filename):
        file = open(filename, "r+")
        for line in file:
            line = line.strip()
            line = line.split(" ")
            self.__grades.append(Grade(int(line[0]), int(line[1]), int(line[2])))
        if len(self.__grades) == 0:
            self.__grades = generate_grades()
        file.close()

    def save_changes(self):
        # function that saves the changes made to the repository
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split("=")[1]
        file.readline()
        if repo_type == "textfiles":
            filename = file.readline().strip().split("=")[1]
            self.save_text_changes(filename)
        elif repo_type == "binaryfiles":
            filename = file.readline().strip().split("=")[1]
            self.save_binary_changes(filename)

    def save_binary_changes(self, filename):
        file = open(filename, "wb+")
        pickle.dump(self.__grades, file)
        file.close()

    def save_text_changes(self, filename):
        # function that saves the changes made to the repository
        file = open(filename, "w+")
        for grade in self.__grades:
            file.write(str(grade.get_student_id()) + " " + str(grade.get_discipline_id()) + " " + str(grade.get_grade_value()) + "\n")
        file.close()

    def add_grade(self, grade: Grade):
        if grade.get_grade_value() < 1 or grade.get_grade_value() > 10:
            raise GradeException()
        self.__grades.append(grade)

    def remove(self, grade):
        self.__grades.remove(grade)

    def undo(self):
        if len(self.undos) == 0:
            raise ValueError("No more undos!")
        self.redos.append(deepcopy(self.__grades))
        self.__grades = self.undos.pop()

    def redo(self):
        if len(self.redos) == 0:
            raise ValueError("No more redos!")
        self.undos.append(deepcopy(self.__grades))
        self.__grades = self.redos.pop()

    def get_all_grades(self):
        return self.__grades

    def remember_state(self):
        self.undos.append(deepcopy(self.__grades))
        self.redos = []
