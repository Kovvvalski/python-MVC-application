from model.repository.student_repository import StudentRepository
from exception.repository_exception import RepositoryException
from exception.service_exception import ServiceException
from model.entity.student import Student
from log.my_logger import logger


class StudentService:

    def __init__(self, repository: StudentRepository):
        self._repository = repository

    def find_student(self, first_name, second_name, third_name, course, group, tasks,
                     completed_tasks, language) -> Student:
        try:
            out = self._repository.find_student(first_name, second_name, third_name, course, group, tasks,
                                                completed_tasks, language)

        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error during getting data from repository', e)

        return out

    def find_by_not_completed_tasks(self, not_completed_tasks: int) -> list[Student]:
        try:
            return self._repository.find_by_not_completed_tasks(not_completed_tasks)
        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error while getting data from', e)

    def find_all(self) -> list[Student]:
        try:
            out = self._repository.find_all()
        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error during getting data from repository', e)
        return out

    def find_by_name(self, first_name: str, second_name: str, third_name: str) -> list[Student]:
        try:
            return self._repository.find_by_name(first_name, second_name, third_name)
        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error during getting data from repository', e)

    def find_by_language(self, language: str) -> list[Student]:
        try:
            return self._repository.find_by_language(language)
        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error during getting data from repository', e)

    def find_by_completed_tasks(self, completed_tasks: int) -> list[Student]:
        try:
            return self._repository.find_by_completed_tasks(completed_tasks)
        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error during getting data from repository', e)

    def find_by_id(self, idtf: int) -> Student:
        try:
            out = self._repository.find_by_id(idtf)
        except RepositoryException as e:
            logger.error('Error during getting data from repository')
            raise ServiceException('Error while getting data from repository', e)

        if out is None:
            logger.warn('Trying to get student with wrong id')
            raise ServiceException('No student with this id')

        return out

    def add_student(self, student: Student):
        if self._is_not_valid(student):
            logger.error('Trying to add incorrect data to repository')
            raise ServiceException('Not correct input data')
        try:
            found = self.find_student(student.first_name, student.second_name, student.third_name, student.course,
                                      student.group, student.tasks, student.completed_tasks, student.language)
            if found is None:
                self._repository.add_student(student)
                logger.info('Student ' + student.first_name + ' ' + student.second_name + ' was added')
            else:
                logger.warn('Trying to add existing student')
                raise ServiceException('Such student already exists')
        except RepositoryException as e:
            logger.error('Error during updating repository')
            raise ServiceException('Error while updating repository', e)

    def add_all(self, students: list[Student]) -> None:
        for student in students:
            if self._is_not_valid(student):
                logger.error('Trying to add incorrect data to repository')
                raise ServiceException('Not correct input data')

            found = self.find_student(student.first_name, student.second_name, student.third_name,
                                      student.course, student.group, student.tasks, student.completed_tasks,
                                      student.language)

            if found is not None:
                logger.error('Student ' + student.first_name + ' ' + student.second_name + ' is already exists')
                raise ServiceException(
                    'Student ' + student.first_name + ' ' + student.second_name + ' is already exists')

        try:
            self._repository.add_all(students)
            logger.info(str(len(students)) + ' students were added')
        except RepositoryException as e:
            logger.error('Error during updating repository')
            raise ServiceException('Error while updating repository', e)

    def delete_student(self, student: Student) -> None:
        try:
            self._repository.delete_student(student)
            logger.info('Student ' + student.first_name + ' ' + student.second_name + ' was deleted')
        except RepositoryException as e:
            logger.error('Error during updating repository')
            raise ServiceException('Error while updating repository', e)

    def update_student(self, student: Student) -> None:
        if self._is_not_valid(student):
            logger.error('Trying to add incorrect data to repository')
            raise ServiceException('Not correct input data')

        try:
            self._repository.update_student(student)
            logger.info('Student ' + student.first_name + ' ' + student.second_name + ' was updated')
        except RepositoryException as e:
            logger.error('Error during updating repository')
            raise ServiceException('Error while updating repository', e)

    def delete_by_name(self, first_name: str, last_name: str, third_name: str) -> int:
        try:
            return self._repository.delete_by_name(first_name, last_name, third_name)
        except Exception as e:
            logger.error('Error while executing query')
            raise ServiceException('Error while executing query', e)

    def delete_by_language(self, language: str) -> int:
        try:
            return self._repository.delete_by_language(language)
        except Exception as e:
            raise ServiceException('Error while executing query', e)

    def delete_by_completed_tasks(self, completed_tasks: int) -> int:
        try:
            return self._repository.delete_by_completed_tasks(completed_tasks)
        except Exception as e:
            logger.error('Error while executing query')
            raise ServiceException('Error while executing query', e)

    def delete_by_not_completed_tasks(self, not_completed_tasks: int) -> int:
        try:
            return self._repository.delete_by_not_completed_tasks(not_completed_tasks)
        except Exception as e:
            logger.error('Error while executing query')
            raise ServiceException('Error while executing query', e)

    @staticmethod
    def _is_not_valid(student: Student) -> bool:
        return (student.course <= 0 or student.course >= 5 or student.completed_tasks < 0 or student.completed_tasks > student.tasks
                or student.language not in ['Java', 'cxx', 'Python'])
