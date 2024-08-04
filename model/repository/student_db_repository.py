from model.entity.student import Student
from model.repository.student_repository import StudentRepository
from exception.repository_exception import RepositoryException

FIND_SQL = ('SELECT id, first_name, second_name, third_name, course, `group`, tasks, completed_tasks, `language` '
            'FROM students.students WHERE first_name = %s AND second_name = %s AND third_name = %s AND course = %s '
            'AND `group` = %s AND tasks = %s AND completed_tasks = %s AND `language` = %s')

FIND_ALL_SQL = (
    'SELECT id, first_name, second_name, third_name, course, `group`, tasks, completed_tasks, `language` '
    'FROM students.students')

FIND_BY_ID_SQL = ('SELECT id, first_name, second_name, third_name, course, `group`, tasks, completed_tasks, `language` '
                  'FROM students.students WHERE id = %s')

ADD_SQL = ('INSERT INTO students.students (first_name, second_name, third_name, course, `group`, tasks,'
           ' completed_tasks, `language`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)')

UPDATE_SQL = ('UPDATE students.students SET first_name = %s, second_name = %s, third_name = %s, course = %s, '
              '`group` = %s, tasks = %s, completed_tasks = %s, `language` = %s WHERE id = %s')

DELETE_BY_ID_SQL = 'DELETE FROM students.students WHERE id = %s'

DELETE_BY_NAME_SQL = "DELETE FROM students.students WHERE first_name = %s AND second_name = %s AND third_name = %s"

DELETE_BY_LANGUAGE_SQL = "DELETE FROM students.students WHERE language = %s"

DELETE_BY_COMPLETED_TASKS_SQL = "DELETE FROM students.students WHERE completed_tasks = %s"

DELETE_BY_NOT_COMPLETED_TASKS = "DELETE FROM students.students WHERE tasks - completed_tasks = %s"

FIND_BY_NAME_SQL = (
    'SELECT id, first_name, second_name, third_name, course, `group`, tasks, completed_tasks, `language` '
    'FROM students.students WHERE first_name = %s and second_name = %s and third_name = %s')

FIND_BY_LANG_SQL = (
    'SELECT id, first_name, second_name, third_name, course, `group`, tasks, completed_tasks, `language` '
    'FROM students.students WHERE `language` = %s')

FIND_BY_CT_SQL = ('SELECT id, first_name, second_name, third_name, course, `group`, tasks, completed_tasks, `language` '
                  'FROM students.students WHERE completed_tasks = %s')


class StudentDbRepository(StudentRepository):

    def __init__(self, connection):
        self.connection = connection

    def find_student(self, first_name, second_name, third_name, course, group, tasks, completed_tasks,
                     language) -> Student:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(FIND_SQL, (first_name, second_name, third_name, course, group, tasks,
                                      completed_tasks, language))
            rows = cursor.fetchall()
            if len(rows) != 1:
                out = None
            else:
                out = Student(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6],
                              rows[0][7], rows[0][8])

        except Exception as e:
            raise RepositoryException('Error during executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

        return out

    def find_all(self) -> list[Student]:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(FIND_ALL_SQL)
            rows = cursor.fetchall()
            out = []
            for row in rows:
                student = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                out.append(student)

        except Exception as e:
            raise RepositoryException('Error during executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

        return out

    def find_by_not_completed_tasks(self, not_completed_tasks: int) -> list[Student]:
        found = self.find_all()
        return list(filter(lambda student: student.tasks - student.completed_tasks == not_completed_tasks, found))

    def find_by_id(self, idtf: int) -> Student:
        out = None
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(FIND_BY_ID_SQL, (idtf,))
            row = cursor.fetchone()
            if row is not None:
                out = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

        except Exception as e:
            raise RepositoryException('Error during executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

        return out

    def find_by_name(self, first_name: str, second_name: str, third_name: str) -> list[Student]:
        out = []
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(FIND_BY_NAME_SQL, (first_name, second_name, third_name))
            rows = cursor.fetchall()
            for row in rows:
                out.append(Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

        except Exception as e:
            raise RepositoryException('Error during executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

        return out

    def find_by_language(self, language: str) -> list[Student]:
        out = []
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(FIND_BY_LANG_SQL, (language,))
            rows = cursor.fetchall()
            for row in rows:
                out.append(Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

        except Exception as e:
            raise RepositoryException('Error during executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

        return out

    def find_by_completed_tasks(self, completed_tasks: int) -> list[Student]:
        out = []
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(FIND_BY_CT_SQL, (completed_tasks,))
            rows = cursor.fetchall()
            for row in rows:
                out.append(Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

        except Exception as e:
            raise RepositoryException('Error during executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

        return out

    def add_student(self, student: Student) -> None:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(ADD_SQL, (student.first_name, student.second_name, student.third_name,
                                     student.course, student.group, student.tasks, student.completed_tasks,
                                     student.language))

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def add_all(self, students: list[Student]) -> None:
        cursor = None
        try:
            cursor = self.connection.cursor()
            for student in students:
                cursor.execute(ADD_SQL, (student.first_name, student.second_name, student.third_name,
                                         student.course, student.group, student.tasks, student.completed_tasks,
                                         student.language))

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def update_student(self, student: Student) -> None:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(UPDATE_SQL, (student.first_name, student.second_name, student.third_name, student.course,
                                        student.group, student.tasks, student.completed_tasks, student.language,
                                        student.idtf))

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def delete_student(self, student: Student) -> None:
        found_student = self.find_student(student.first_name, student.second_name, student.third_name,
                                          student.course, student.group, student.tasks, student.completed_tasks,
                                          student.language)

        if found_student is None:
            return

        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(DELETE_BY_ID_SQL, (found_student.idtf,))

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def delete_by_name(self, first_name: str, second_name: str, third_name: str) -> int:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(DELETE_BY_NAME_SQL, (first_name, second_name, third_name))
            return cursor.rowcount

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def delete_by_language(self, language: str) -> int:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(DELETE_BY_LANGUAGE_SQL, (language,))
            return cursor.rowcount

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def delete_by_completed_tasks(self, completed_tasks: int) -> int:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(DELETE_BY_COMPLETED_TASKS_SQL, (completed_tasks,))
            return cursor.rowcount

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()

    def delete_by_not_completed_tasks(self, not_completed_tasks: int) -> int:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(DELETE_BY_NOT_COMPLETED_TASKS, (not_completed_tasks,))
            return cursor.rowcount

        except Exception as e:
            raise RepositoryException('Error while executing query', e)

        finally:
            if cursor is not None:
                cursor.close()
