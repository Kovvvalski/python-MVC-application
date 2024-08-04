import os
from model.repository.student_xml_repository import StudentXmlRepository
from model.service.student_service import StudentService
from view.find_window import FindWindow
from view.students_view import StudentsView
from view.new_student import NewStudent
from view.delete_window import DeleteWindow
from view.alternative_view_window import AlternativeViewWindow
from model.repository.student_db_repository import StudentDbRepository
from dbconnection.connection_pool import connection


class StudentsController(object):
    def __init__(self, service: StudentService, view: StudentsView):
        self.service = service

        self.view = view
        self.view.next_button["command"] = lambda: self.change_page(self.current_page + 1)
        self.view.prev_button["command"] = lambda: self.change_page(self.current_page - 1)
        self.view.change_rows_button["command"] = self.change_rows
        self.view.btn_new["command"] = self.create_student
        self.view.first_page_button["command"] = lambda: self.change_page(1)
        self.view.last_page_button["command"] = lambda: self.change_page(self._count_max_page())
        self.view.find_button["command"] = self.open_find_window
        self.view.delete_button["command"] = self.open_delete_window
        self.view.tree_button["command"] = self.show_tree_window
        self.view.confirm_button["command"] = self.change_datasource

        self.view.first_page_button["text"] = "1"
        self.view.last_page_button["text"] = ""

        self.students = []
        self.rows_on_page = 10
        self.current_page = 0

    def start(self):
        self.students = self.service.find_all()
        self.view.last_page_button["text"] = str(self._count_max_page())
        self.change_page(1)
        self.view.mainloop()

    def change_datasource(self):
        if self.view.condition_var.get() == "Database":
            self.service._repository = StudentDbRepository(connection)
        else:
            new_datasource = self.view.show_change_datasource_dialog()
            if new_datasource is None:
                return
            path = "resources/" + new_datasource + ".xml"
            if os.path.exists(path):
                self.service._repository = StudentXmlRepository(path)
            else:
                self.view.show_file_not_found_dialog()
                return

        self.students = self.service.find_all()
        self.view.last_page_button["text"] = str(self._count_max_page())
        self.change_page(1)

    def show_tree_window(self):
        tree_window = AlternativeViewWindow(self.view)
        tree_window.tree.populate_tree(self.students)

    def open_delete_window(self):
        delete_window = DeleteWindow(self.view)
        delete_window.delete_button["command"] = lambda: self.delete_by_condition(delete_window.condition_var.get())

    def delete_by_condition(self, condition: str):
        count = 0
        if condition == "By name":
            names = self.view.show_enter_name_dialog()
            if len(names) == 3:
                count = self.service.delete_by_name(names[0], names[1], names[2])
        elif condition == "By language":
            language = self.view.show_enter_language_dialog()
            count = self.service.delete_by_language(language)
        elif condition == "By completed tasks":
            tasks = self.view.show_enter_tasks_dialog()
            count = self.service.delete_by_completed_tasks(tasks)
        else:
            tasks = self.view.show_enter_tasks_dialog()
            count = self.service.delete_by_not_completed_tasks(tasks)

        self.students = self.service.find_all()
        self.change_page(1)
        self.view.show_delete_info(count)

    def open_find_window(self):
        find_window = FindWindow(self.view)
        find_window.search_button["command"] = lambda: self.find_by_condition(find_window.condition_var.get(),
                                                                              find_window)

    def find_by_condition(self, condition: str, find_window: FindWindow):
        found = None
        if condition == "By name":
            names = self.view.show_enter_name_dialog()
            if len(names) == 3:
                found = self.service.find_by_name(names[0], names[1], names[2])
        elif condition == "By language":
            language = self.view.show_enter_language_dialog()
            found = self.service.find_by_language(language)
        elif condition == "By completed tasks":
            tasks = self.view.show_enter_tasks_dialog()
            found = self.service.find_by_completed_tasks(tasks)
        else:
            tasks = self.view.show_enter_tasks_dialog()
            found = self.service.find_by_not_completed_tasks(tasks)

        find_window.list.populate_tree(found)

    def change_page(self, new_page: int):
        max_page = self._count_max_page()
        if max_page == 0:
            self.view.list.populate_tree([])
        if 0 < new_page <= max_page:
            new_students = []
            for i in range(self.rows_on_page * (new_page - 1), (
                    self.rows_on_page * new_page if
                    self.rows_on_page * new_page <= len(self.students)
                    else len(self.students))):
                new_students.append(self.students[i])
                self.view.list.populate_tree(new_students)
            self.view.list.populate_tree(new_students)
            self.current_page = new_page
            self.view.current_page["text"] = str(self.current_page)

    def change_rows(self):
        new_rows = self.view.show_change_rows_dialog()
        if new_rows is not None:
            self.rows_on_page = new_rows
        self.current_page = 1
        self.view.last_page_button["text"] = str(self._count_max_page())
        self.change_page(1)

    def create_student(self):
        new_student = NewStudent(self.view).show()
        if new_student:
            try:
                self.service.add_student(new_student)
                self.students.append(new_student)
                self.change_page(self.current_page)
            except Exception:
                error_str = ('Incorrect student' + "\n" +
                             new_student.first_name + "\n" +
                             new_student.second_name + "\n" +
                             new_student.third_name + "\n" +
                             str(new_student.course) + "\n" +
                             new_student.group + "\n" +
                             str(new_student.tasks) + "\n" +
                             str(new_student.completed_tasks) + "\n" +
                             new_student.language + "\n"
                             )
                self.view.show_error_dialog(error_str)

    def _count_max_page(self) -> int:
        students = len(self.students)
        max_page = students // self.rows_on_page
        max_page += 1 if students - max_page * self.rows_on_page else 0
        return max_page
