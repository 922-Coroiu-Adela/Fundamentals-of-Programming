from copy import deepcopy
from random import randint

from src.domain.ComplexNumber import ComplexNumber

class MemoryRepository:
    def __init__(self):
        self.complex_numbers = self.generate_random_complex_numbers(10)
        self.undo_list = []


    def add(self, complex_number: ComplexNumber):
        '''
        Adds a complex number to the list of complex numbers in the repository,
        and adds the previous list to the undo list
        :param complex_number: the complex number to be added
        :return: -
        '''
        self.undo_list.append(deepcopy(self.complex_numbers))
        self.complex_numbers.append(complex_number)

    def filter(self, start: int, end: int):
        self.undo_list.append(deepcopy(self.complex_numbers))
        self.complex_numbers = self.complex_numbers[start:end + 1]

    def get_all(self):
        return self.complex_numbers

    def generate_random_complex_numbers(self, number_of_complex_numbers: int):
        real = randint(-100, 100)
        imaginary = randint(-100, 100)
        rand_list = []
        for i in range(number_of_complex_numbers):
            rand_list.append(ComplexNumber(real, imaginary))
            real = randint(-100, 100)
            imaginary = randint(-100, 100)

        return rand_list

    def undo(self):
        if len(self.undo_list) == 0:
            raise ValueError("No more undos!")
        self.complex_numbers = self.undo_list.pop()

    def save_changes(self):
        pass
