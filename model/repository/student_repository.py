from abc import ABC, abstractmethod
from model.entity.student import Student


class StudentRepository(ABC):

    @abstractmethod
    def find_student(self, first_name, second_name, third_name, course, group, tasks, completed_tasks,
                     language) -> Student:
        pass

    @abstractmethod
    def find_all(self) -> list[Student]:
        pass

    @abstractmethod
    def find_by_not_completed_tasks(self, not_completed_tasks: int) -> list[Student]:
        pass

    @abstractmethod
    def find_by_id(self, idtf: int) -> Student:
        pass

    @abstractmethod
    def find_by_name(self, first_name: str, second_name: str, third_name: str) -> list[Student]:
        pass

    @abstractmethod
    def find_by_language(self, language: str) -> list[Student]:
        pass

    @abstractmethod
    def find_by_completed_tasks(self, completed_tasks: int) -> list[Student]:
        pass

    @abstractmethod
    def add_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def add_all(self, students: list[Student]) -> None:
        pass

    @abstractmethod
    def delete_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def delete_by_name(self, first_name: str, second_name: str, third_name: str) -> int:
        pass

    @abstractmethod
    def delete_by_language(self, language: str) -> int:
        pass

    @abstractmethod
    def delete_by_completed_tasks(self, completed_tasks: int) -> int:
        pass

    @abstractmethod
    def delete_by_not_completed_tasks(self, not_completed_tasks: int) -> int:
        pass
