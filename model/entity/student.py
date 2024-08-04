class Student:
    def __init__(self, idtf: int, first_name: str, second_name: str, third_name: str, course: int,
                 group: str, tasks: int, completed_tasks: int, language: str):
        self.idtf = idtf
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name
        self.course = course
        self.group = group
        self.tasks = tasks
        self.completed_tasks = completed_tasks
        self.language = language
