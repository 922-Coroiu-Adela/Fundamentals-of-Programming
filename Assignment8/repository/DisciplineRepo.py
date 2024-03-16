import pickle
from copy import deepcopy

from src.MyExceptions import ExistingDiscipline
from src.domain.Discipline import Discipline
from src.repository.GenerateEntries import generate_disciplines
class DisciplineRepo:
    def __init__(self):
        self.__disciplines = []
        self.undos = []
        self.redos = []
        self.pick_discipline_repository()

    def pick_discipline_repository(self):
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split("=")[1]
        if repo_type == "inmemory":
            self.__disciplines = generate_disciplines()
        elif repo_type == "textfiles":
            # now we have to read the filename
            filename = file.readline().strip().split("=")[1]    # filename = "disciplines.txt"
            self.load_text_data(filename)
        elif repo_type == "binaryfiles":
            # now we have to read the filename
            filename = file.readline().strip().split("=")[1]
            self.load_binary_data(filename)

    def load_binary_data(self, filename):
        file = open(filename, "rb+")
        try:
            aux = pickle.load(file)
        except EOFError:
            aux = []

        if len(aux) == 0:
            aux = generate_disciplines()
        self.__disciplines = aux
        file.close()

    def load_text_data(self, filename):
        file = open(filename, "r+")
        for line in file:
            line = line.strip()
            line = line.split(" ")
            self.__disciplines.append(Discipline(int(line[0]), line[1]))
        if len(self.__disciplines) == 0:
            self.__disciplines = generate_disciplines()
        file.close()

    def save_changes(self):
        # function that saves the changes made to the repository
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split("=")[1]
        if repo_type == "textfiles":
            filename = file.readline().strip().split("=")[1]
            self.save_text_changes(filename)
        elif repo_type == "binaryfiles":
            filename = file.readline().strip().split("=")[1]
            self.save_binary_changes(filename)

    def save_binary_changes(self, filename):
        file = open(filename, "wb+")
        pickle.dump(self.__disciplines, file)
        file.close()

    def save_text_changes(self, filename):
        # function that saves the changes made to the repository
        file = open(filename, "w+")
        for discipline in self.__disciplines:
            file.write(str(discipline.get_discipline_id()) + " " + discipline.get_name() + "\n")
        file.close()

    def undo(self):
        if len(self.undos) == 0:
            raise ValueError("No more undos!")
        self.redos.append(deepcopy(self.__disciplines))
        self.__disciplines = self.undos.pop()

    def redo(self):
        if len(self.redos) == 0:
            raise ValueError("No more redos!")
        self.undos.append(deepcopy(self.__disciplines))
        self.__disciplines = self.redos.pop()

    def add_discipline(self, discipline: Discipline):
        for d in self.__disciplines:
            if discipline.get_discipline_id() == d.get_discipline_id():
                raise ExistingDiscipline()
        self.__disciplines.append(discipline)

    def remove(self, discipline):
        self.__disciplines.remove(discipline)

    def update(self, discipline):
        for i in range(len(self.__disciplines)):
            if self.__disciplines[i] == discipline:
                self.__disciplines[i] = discipline

    def remember_state(self):
        self.undos.append(deepcopy(self.__disciplines))
        self.redos = []

    def get_all_disciplines(self):
        return self.__disciplines

