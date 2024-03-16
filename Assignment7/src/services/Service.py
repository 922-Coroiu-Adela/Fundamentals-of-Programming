from src.repository.MemoryRepository import MemoryRepository
from src.repository.TextFileRepository import TextFileRepository
from src.repository.BinaryFileRepository import BinaryFileRepository

class Service:
    def __init__(self):
        self.repository = self.pick_repository()

    def pick_repository(self):
        file = open("settings.properties", "r")
        repo_type = file.readline().strip().split(":")[1]
        if repo_type == "memory":
            return MemoryRepository()
        elif repo_type == "text":
            return TextFileRepository()
        elif repo_type == "binary":
            return BinaryFileRepository()

    def add(self, complex_number):
        '''
        Adds a complex number to the repository
        :param complex_number: the complex number to be added
        :return: -
        '''
        self.repository.add(complex_number)

    def filter(self, start, end):
        self.repository.filter(start, end)

    def get_all(self):
        return self.repository.get_all()

    def save_changes(self):
        self.repository.save_changes()

    def undo(self):
        self.repository.undo()