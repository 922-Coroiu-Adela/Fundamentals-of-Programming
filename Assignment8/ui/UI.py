from src.services.Service import Service
from src.MyExceptions import *

class UI:
    def __init__(self):
        self.service = Service()

    def display_students(self):
        students = self.service.get_all_students()
        for student in students:
           print(student.to_string())

    def display_disciplines(self):
        disciplines = self.service.get_all_disciplines()
        for discipline in disciplines:
            print(discipline.to_string())

    def display_grades(self):
        grades = self.service.get_all_grades()
        for grade in grades:
            print(grade.to_string())

    def print_the_grades_of_a_student(self, result):
        # result is a list of lists
        # each list has 2 elements: the name of the discipline and the grades at that discipline
        # the grades at that discipline is a list of grades
        for i in range(len(result)):
            print(result[i][0])
            for j in range(len(result[i][1])):
                print(result[i][1][j].to_string())

    def print_the_grades_of_a_discipline(self, result):
        # result is a list of lists
        # each list has 2 elements: the name of the student and the grade at that discipline
        for i in range(len(result)):
            print(result[i][0])
            print(result[i][1])

    def print_main_menu(self):
        print("1. Student related operations")
        print("2. Discipline related operations")
        print("3. Grade related operations")
        print("4. Statistics")
        print("0. Exit")

    def main_run(self):
        while True:
            self.print_main_menu()
            command = input("Enter command: ")
            if command == "0":
                self.service.save_changes()
                break
            elif command == "1":
                self.run_student_related()
            elif command == "2":
                self.run_discipline_related()
            elif command == "3":
                self.run_grade_related()
            elif command == "4":
                self.run_statistics()
            else:
                print("Invalid command!")

    def print_student_related_menu(self):
        print("1. Add a student")
        print("2. Delete a student and all their grades")
        print("3. Display all students")
        print("4. Search for students")
        print("5. Display the grades of a student")
        print("6. Undo")
        print("7. Redo")
        print("0. Exit")

    def run_student_related(self):
        while True:
            self.print_student_related_menu()
            command = input("Enter command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    student_id = int(input("Enter student id: "))
                    student_name = input("Enter student name: ")
                    self.service.add_student(student_id, student_name)
                except ValueError:
                    print("Invalid id!")
                except ExistingStudent as ex:
                    print("ERROR:", ex.message)
            elif command == "2":
                try:
                    student_id = int(input("Enter student id: "))
                    self.service.delete_student_and_grades(student_id)
                except ValueError:
                    print("Invalid id!")
                except ExistenceStudent as ex:
                    print("ERROR: ", ex.message)
            elif command == "3":
                self.display_students()
            elif command == "4":
                search_string = input("Enter search string: ")
                students = self.service.search_students(search_string)
                for student in students:
                    print(student.to_string())
            elif command == "5":
                try:
                    student_id = int(input("Enter student id: "))
                    result = self.service.get_grades_of_student(student_id)
                    self.print_the_grades_of_a_student(result)
                except ValueError:
                    print("Invalid id!")
                except ExistenceStudent as ex:
                    print("ERROR: ", ex.message)
            elif command == "6":
                try:
                    self.service.undo()
                except ValueError as ex:
                    print("ERROR: ", ex)
            elif command == "7":
                try:
                    self.service.redo()
                except ValueError as ex:
                    print("ERROR: ", ex)
            else:
                print("Invalid command!")

    def print_discipline_related_menu(self):
        print("1. Add a discipline")
        print("2. Delete a discipline and all its grades")
        print("3. Display all disciplines")
        print("4. Search for disciplines")
        print("5. Display the grades of a discipline")
        print("6. Undo")
        print("7. Redo")
        print("0. Exit")

    def run_discipline_related(self):
        while True:
            self.print_discipline_related_menu()
            command = input("Enter command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    discipline_id = int(input("Enter discipline id: "))
                    discipline_name = input("Enter discipline name: ")
                    self.service.add_discipline(discipline_id, discipline_name)
                except ValueError:
                    print("Invalid id!")
                except ExistingDiscipline as ex:
                    print("ERROR: ", ex.message)
            elif command == "2":
                try:
                    discipline_id = int(input("Enter discipline id: "))
                    self.service.delete_discipline_and_grades(discipline_id)
                except ValueError:
                    print("Invalid id!")
                except ExistenceDiscipline as ex:
                    print("ERROR: ", ex.message)
            elif command == "3":
                self.display_disciplines()
            elif command == "4":
                search_string = input("Enter search string: ")
                disciplines = self.service.search_disciplines(search_string)
                for discipline in disciplines:
                    print(discipline.to_string())
            elif command == "5":
                try:
                    discipline_id = int(input("Enter discipline id: "))
                    result = self.service.get_all_grades_for_discipline(discipline_id)
                    self.print_the_grades_of_a_discipline(result)
                except ValueError:
                    print("Invalid id!")
                except ExistenceDiscipline as ex:
                    print("ERROR: ", ex.message)
            elif command == "6":
                try:
                    self.service.undo()
                except ValueError as ex:
                    print("ERROR: ", ex)
            elif command == "7":
                try:
                    self.service.redo()
                except ValueError as ex:
                    print("ERROR: ", ex)
            else:
                print("Invalid command!")

    def print_grade_related_menu(self):
        print("1. Add a grade")
        print("2. Display all grades")
        print("3. Undo")
        print("4. Redo")
        print("0. Exit")

    def run_grade_related(self):
        while True:
            self.print_grade_related_menu()
            command = input("Enter command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    discipline_id = int(input("Enter discipline id: "))
                    student_id = int(input("Enter student id: "))
                    grade_value = int(input("Enter grade value: "))
                    self.service.add_grade(discipline_id, student_id, grade_value)
                except ValueError:
                    print("Invalid id or grade value!")
                except ExistenceDiscipline as ex:
                    print("ERROR: ", ex.message)
                except ExistenceStudent as ex:
                    print("ERROR: ", ex.message)
                except GradeException as ex:
                    print("ERROR: ", ex.message)
            elif command == "2":
                self.display_grades()
            elif command == "3":
                try:
                    self.service.undo()
                except ValueError as ex:
                    print("ERROR: ", ex)
            elif command == "4":
                try:
                    self.service.redo()
                except ValueError as ex:
                    print("ERROR: ", ex)
            else:
                print("Invalid command!")

    def print_statistics_menu(self):
        print("0. Exit")
        print("1. Display all students failing at one or more disciplines")
        print("2. Display all students with the best school situation")
        print("3. Display all disciplines at which there is at least one grade,"
              "sorted descending by average grade")

    def run_statistics(self):
        while True:
            self.print_statistics_menu()
            command = input("Enter command: ")
            if command == "0":
                break
            elif command == "1":
                students = self.service.students_failing()
                for student in students:
                    print(student.to_string())
            elif command == "2":
                students = self.service.display_students_best_situation()
                for student in students:
                    print(student[0], student[1])
            elif command == "3":
                try:
                    disciplines = self.service.disciplines_sorted_by_average()
                    for discipline in disciplines:
                        print(discipline[0], discipline[1])
                except ExistenceDiscipline as ex:
                    print("ERROR: ", ex.message)
            else:
                print("Invalid command!")