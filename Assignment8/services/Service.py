from src.MyExceptions import ExistenceDiscipline, ExistenceStudent
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.domain.Student import Student
from src.repository.DisciplineRepo import DisciplineRepo
from src.repository.GradeRepo import GradeRepo
from src.repository.StudentRepo import StudentRepo


class Service:
    def __init__(self):
        self.__students_repo = StudentRepo()
        self.__grades_repo = GradeRepo()
        self.__discipline_repo = DisciplineRepo()

    def add_student(self, student_id, name):
        '''
        Adds a student to the repository
        :param student: the student to be added
        :return: -
        '''
        self.remember_state()
        self.__students_repo.add_student(Student(student_id, name))

    def add_discipline(self, discipline_id, name):
        '''
        Adds a discipline to the repository
        :param discipline: the discipline to be added
        :return: -
        '''
        self.remember_state()
        self.__discipline_repo.add_discipline(Discipline(discipline_id, name))

    def add_grade(self, discipline_id, student_id, grade):
        '''
        Adds a grade to the repository
        :param discipline_id: the id of the discipline
        :param student_id: the id of the student
        :param grade: the grade to be added
        :return:
        '''
        if discipline_id not in [d.get_discipline_id() for d in self.__discipline_repo.get_all_disciplines()]:
            raise ExistenceDiscipline()
        if student_id not in [s.get_student_id() for s in self.__students_repo.get_all_students()]:
            raise ExistenceStudent()
        self.remember_state()
        self.__grades_repo.add_grade(Grade(discipline_id, student_id, grade))


    def disciplines_failed_by_a_student(self, student_id):
        '''
        Returns the disciplines failed by a student
        :param student_id: the id of the student
        :return: a list of disciplines
        '''
        if student_id not in [s.get_student_id() for s in self.__students_repo.get_all_students()]:
            raise ExistenceStudent()
        count = 0
        for d in self.__discipline_repo.get_all_disciplines():
            sum = 0
            nr = 0
            for g in self.__grades_repo.get_all_grades():
                if g.get_discipline_id() == d.get_discipline_id() and g.get_student_id() == student_id:
                    sum += g.get_grade_value()
                    nr += 1
            if nr != 0:
                if sum / nr < 5:
                    count += 1
        return count

    def students_failing(self):
        '''
        Returns the students failing a discipline
        :param discipline_id: the id of the discipline
        :return: a list of students
        '''
        result = []
        for student in self.__students_repo.get_all_students():
            if self.disciplines_failed_by_a_student(student.get_student_id()) > 0:
                result.append(student)
        return result

    def student_average_of_disciplines(self, student_id):
        '''
        Returns the average of the grades of a student
        :param student_id: the id of the student
        :return: a float number
        '''
        if student_id not in [s.get_student_id() for s in self.__students_repo.get_all_students()]:
            raise ExistenceStudent()
        sum = 0
        nr = 0
        for discipline in self.__discipline_repo.get_all_disciplines():
            sum1 = 0
            nr1 = 0
            for grade in self.__grades_repo.get_all_grades():
                if grade.get_discipline_id() == discipline.get_discipline_id() and grade.get_student_id() == student_id:
                    sum1 += grade.get_grade_value()
                    nr1 += 1
            if nr1 != 0:
                sum += sum1 / nr1
                nr += 1
        if nr == 0:
            return 0
        return sum / nr

    def display_students_best_situation(self):
        '''
        Displays the students with the best situation
        :return: -
        '''
        students_average = []
        for student in self.__students_repo.get_all_students():
            students_average.append([student.get_name(), self.student_average_of_disciplines(student.get_student_id())])

        # sort students_average by their average of the grades
        for i in range(len(students_average) - 1):
            for j in range(i + 1, len(students_average)):
                if students_average[i][1] < students_average[j][1]:
                    students_average[i], students_average[j] = students_average[j], students_average[i]

        return students_average

    def discipline_average(self, discipline_id):
        '''
        Returns the average of the grades of a discipline
        :param discipline_id: the id of the discipline
        :return:
        '''
        if discipline_id not in [d.get_discipline_id() for d in self.__discipline_repo.get_all_disciplines()]:
            raise ExistenceDiscipline()
        # we compute the average of the grades of the discipline
        sum = 0
        nr = 0
        for grade in self.__grades_repo.get_all_grades():
            if grade.get_discipline_id() == discipline_id:
                sum += grade.get_grade_value()
                nr += 1
        if nr == 0:
            return 0
        return sum / nr

    def disciplines_sorted_by_average(self):
        '''
        Displays the disciplines sorted by average
        :return: -
        '''
        disciplines_average = []
        for discipline in self.__discipline_repo.get_all_disciplines():
            disciplines_average.append([discipline.get_name(), self.discipline_average(discipline.get_discipline_id())])

        # keep only the disciplines with at least one grade
        disciplines_average = [d for d in disciplines_average if d[1] != 0]

        disciplines_average.sort(key=lambda x: x[1], reverse=True)

        return disciplines_average

    def get_all_students(self):
        '''
        Returns all the students in the repository
        :return: a list of students
        '''
        return self.__students_repo.get_all_students()

    def get_all_disciplines(self):
        '''
        Returns all the disciplines in the repository
        :return: a list of disciplines
        '''
        return self.__discipline_repo.get_all_disciplines()

    def get_grades_of_student_on_discipline(self, student_id, discipline_id):
        '''
        Returns the grades of a student on a discipline
        :param student_id: the id of the student
        :param discipline_id: the id of the discipline
        :return:
        '''
        result = []
        for grade in self.__grades_repo.get_all_grades():
            if grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id:
                result.append(grade)
        return result

    def get_grades_of_student(self, student_id):
        '''
        Returns the grades of a student
        :param student_id: the id of the student
        :return: a list of grades
        '''
        result = []
        # for each discipline, we add the name of the discipline and the grades of the student on that discipline
        for discipline in self.__discipline_repo.get_all_disciplines():
            grades = self.get_grades_of_student_on_discipline(student_id, discipline.get_discipline_id())
            if len(grades) != 0:
                result.append([discipline.get_name(), grades])
        return result

    def get_all_grades(self):
        '''
        Returns all the grades in the repository
        :return: a list of grades
        '''
        return self.__grades_repo.get_all_grades()

    def search_students(self, search_string):
        '''
        Searches for students whose id or name contain a given string
        :param search_string: the string to be searched for
        :return: a list of students
        '''
        search_string = search_string.lower()
        result = []
        for student in self.__students_repo.get_all_students():
            str_id = str(student.get_student_id())
            if search_string in str_id or search_string in student.get_name().lower():
                result.append(student)
        return result

    def search_disciplines(self, search_string):
        '''
        Searches for disciplines whose id or name contain a given string
        :param search_string: the string to be searched for
        :return: a list of disciplines
        '''
        search_string = search_string.lower()
        result = []
        for discipline in self.__discipline_repo.get_all_disciplines():
            str_id = str(discipline.get_discipline_id())
            if search_string in str_id or search_string in discipline.get_name().lower():
                result.append(discipline)
        return result

    def delete_student_and_grades(self, student_id):
        '''
        Deletes a student and all their grades from the repository
        :param student_id: the id of the student to be deleted
        :return: -
        '''
        if student_id not in [s.get_student_id() for s in self.__students_repo.get_all_students()]:
            raise ExistenceStudent()

        self.remember_state()

        filtered_grades = []
        for grade in self.__grades_repo.get_all_grades():
            if grade.get_student_id() != student_id:
                filtered_grades.append(grade)
        for grade in self.__grades_repo.get_all_grades():
            if grade not in filtered_grades:
                self.__grades_repo.remove(grade)

        filtered_students = []
        for student in self.__students_repo.get_all_students():
            if student.get_student_id() != student_id:
                filtered_students.append(student)
        for student in self.__students_repo.get_all_students():
            if student not in filtered_students:
                self.__students_repo.remove(student)

    def delete_discipline_and_grades(self, discipline_id):
        '''
        Deletes a discipline and all its grades from the repository
        :param discipline_id: the id of the discipline to be deleted
        :return: -
        '''
        if discipline_id not in [d.get_discipline_id() for d in self.__discipline_repo.get_all_disciplines()]:
            raise ExistenceDiscipline()

        self.remember_state()

        filtered_grades = []
        for grade in self.__grades_repo.get_all_grades():
            if grade.get_discipline_id() != discipline_id:
                filtered_grades.append(grade)
        for grade in self.__grades_repo.get_all_grades():
            if grade not in filtered_grades:
                self.__grades_repo.remove(grade)

        filtered_disciplines = []
        for discipline in self.__discipline_repo.get_all_disciplines():
            if discipline.get_discipline_id() != discipline_id:
                filtered_disciplines.append(discipline)
        for discipline in self.__discipline_repo.get_all_disciplines():
            if discipline not in filtered_disciplines:
                self.__discipline_repo.remove(discipline)


    def get_all_grades_for_discipline(self, discipline_id):
        '''
        Returns all the grades for a discipline
        :param discipline_id: the id of the discipline
        :return: a list of grades
        '''
        result = []
        for stud in self.__students_repo.get_all_students():
            for grade in self.__grades_repo.get_all_grades():
                if grade.get_discipline_id() == discipline_id and grade.get_student_id() == stud.get_student_id():
                    result.append([stud.get_name(), grade.get_grade_value()])

        return result

    def remember_state(self):
        self.__students_repo.remember_state()
        self.__discipline_repo.remember_state()
        self.__grades_repo.remember_state()

    def undo(self):
        self.__students_repo.undo()
        self.__discipline_repo.undo()
        self.__grades_repo.undo()

    def redo(self):
        self.__students_repo.redo()
        self.__discipline_repo.redo()
        self.__grades_repo.redo()

    def save_changes(self):
        self.__students_repo.save_changes()
        self.__discipline_repo.save_changes()
        self.__grades_repo.save_changes()
