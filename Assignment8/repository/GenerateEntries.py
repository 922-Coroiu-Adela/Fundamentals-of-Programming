names = ['Sarah', 'John', 'Jane', 'Peter', 'Melissa', 'Tom', 'Jerry', 'Morty', 'Rick', 'Morticia',
         'Gomez', 'Wednesday', 'Anna', 'Lana', 'Selena', 'Dory', 'Beth', 'Danny', 'Mickey', 'Minnie']

discipl = ['Math', 'English', 'French', 'German', 'History', 'Geography', 'Biology', 'Chemistry', 'Physics',
                'Computer Science', 'Physical Education', 'Music', 'Art', 'Drama', 'Literature', 'Philosophy',
                'Psychology', 'Sociology', 'Economics', 'Accounting']

grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import random
from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade


def generate_students():
    """
    Generates 20 students with random names
    :return: the list of students
    """
    students = []
    for i in range(20):
        students.append(Student(i, names[random.randint(0, len(names) - 1)]))

    return students

def generate_disciplines():
    """
    Generates 20 disciplines with random names
    :return: the list of disciplines
    """
    disciplines = []
    for i in range(20):
        disciplines.append(Discipline(i, discipl[random.randint(0, len(discipl) - 1)]))

    return disciplines

def generate_grades():
    """
    Generates 100 random grades for the 20 students and 20 disciplines
    :return: the list of grades
    """
    grades = []
    for i in range(20):
        grades.append(Grade(random.randint(0, 19), random.randint(0, 19), random.randint(1, 10)))

    return grades
