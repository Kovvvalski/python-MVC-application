from model.entity.student import Student
from model.repository.student_repository import StudentRepository
from model.xml_processing.parser import Parser
from exception.repository_exception import RepositoryException


class StudentXmlRepository(StudentRepository):
    def __init__(self, path):
        self.path = path
        self.students = Parser.parse(path)

    def find_student(self, first_name, second_name, third_name, course, group, tasks, completed_tasks,
                     language) -> Student:
        out = None
        for student in self.students:
            if (student.first_name == first_name and
                    student.second_name == second_name and
                    student.third_name == third_name and
                    student.course == course and
                    student.group == group and
                    student.tasks == tasks and
                    student.completed_tasks == completed_tasks and
                    student.language == language):
                out = Student(0, student.first_name, student.second_name, student.third_name,
                              student.course, student.group, student.tasks, student.completed_tasks, student.language)
        return out

    def find_all(self) -> list[Student]:
        out = []
        for student in self.students:
            out.append(Student(0, student.first_name, student.second_name, student.third_name,
                               student.course, student.group, student.tasks, student.completed_tasks, student.language))
        return out

    def find_by_not_completed_tasks(self, not_completed_tasks: int) -> list[Student]:
        out = []
        filtered = filter(lambda s: s.tasks - s.completed_tasks == not_completed_tasks, self.students)
        for student in filtered:
            out.append(Student(0, student.first_name, student.second_name, student.third_name,
                               student.course, student.group, student.tasks, student.completed_tasks, student.language))
        return out

    def find_by_id(self, idtf: int) -> Student:
        if idtf < 0 or idtf > len(self.students) - 1:
            raise RepositoryException("No student with this id")

        return Student(self.students[idtf].idtf, self.students[idtf].first_name, self.students[idtf].second_name,
                       self.students[idtf].third_name, self.students[idtf].course, self.students[idtf].group,
                       self.students[idtf].tasks, self.students[idtf].completed_tasks, self.students[idtf].language)

    def find_by_name(self, first_name: str, second_name: str, third_name: str) -> list[Student]:
        out = []
        for student in self.students:
            if (student.first_name == first_name and
                    student.second_name == second_name and
                    student.third_name == third_name):
                out.append(Student(0, student.first_name, student.second_name, student.third_name,
                                   student.course, student.group, student.tasks, student.completed_tasks,
                                   student.language))
        return out

    def find_by_language(self, language: str) -> list[Student]:
        out = []
        for student in self.students:
            if student.language == language:
                out.append(Student(0, student.first_name, student.second_name, student.third_name,
                                   student.course, student.group, student.tasks, student.completed_tasks,
                                   student.language))
        return out

    def find_by_completed_tasks(self, completed_tasks: int) -> list[Student]:
        out = []
        for student in self.students:
            if student.completed_tasks == completed_tasks:
                out.append(Student(0, student.first_name, student.second_name, student.third_name,
                                   student.course, student.group, student.tasks, student.completed_tasks,
                                   student.language))
        return out

    def add_student(self, student: Student) -> None:
        self.students.append(Student(len(self.students), student.first_name, student.second_name, student.third_name,
                                     student.course, student.group, student.tasks, student.completed_tasks,
                                     student.language))
        try:
            Parser.create(self.students, self.path)
        except Exception:
            raise RepositoryException("Error during updating data")

    def add_all(self, students: list[Student]) -> None:
        for student in students:
            self.add_student(student)

    def delete_student(self, student: Student) -> None:
        filtered = []
        for s in self.students:
            if (s.first_name != student.first_name and
                    s.second_name != student.second_name and
                    s.third_name != student.third_name and
                    s.course != student.course and
                    s.group != student.group and
                    s.tasks != student.tasks and
                    s.completed_tasks != student.completed_tasks and
                    s.language != student.language):
                filtered.append(s)
        self.students = filtered
        try:
            Parser.create(self.students, self.path)
        except Exception:
            raise RepositoryException("Error during updating data")

    def delete_by_name(self, first_name: str, second_name: str, third_name: str) -> int:
        filtered = []
        for s in self.students:
            if (s.first_name != first_name and
                    s.second_name != second_name and
                    s.third_name != third_name):
                filtered.append(s)
        out = len(self.students) - len(filtered)
        self.students = filtered
        try:
            Parser.create(self.students, self.path)
            return out
        except Exception:
            raise RepositoryException("Error during updating data")

    def delete_by_language(self, language: str) -> int:
        filtered = []
        for s in self.students:
            if s.language != language:
                filtered.append(s)
        out = len(self.students) - len(filtered)
        self.students = filtered
        try:
            Parser.create(self.students, self.path)
            return out
        except Exception:
            raise RepositoryException("Error during updating data")

    def delete_by_completed_tasks(self, completed_tasks: int) -> int:
        filtered = []
        for s in self.students:
            if s.completed_tasks != completed_tasks:
                filtered.append(s)
        out = len(self.students) - len(filtered)
        self.students = filtered
        try:
            Parser.create(self.students, self.path)
            return out
        except Exception:
            raise RepositoryException("Error during updating data")

    def delete_by_not_completed_tasks(self, not_completed_tasks: int) -> int:
        filtered = []
        for s in self.students:
            if s.tasks - s.completed_tasks != not_completed_tasks:
                filtered.append(s)
        out = len(self.students) - len(filtered)
        self.students = filtered
        try:
            Parser.create(self.students, self.path)
            return out
        except Exception:
            raise RepositoryException("Error during updating data")
