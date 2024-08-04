import tkinter as tk
from model.entity.student import Student
import tkinter.messagebox as mb


class StudentForm(tk.LabelFrame):
    fields = ("first name", "second name", "third name", "course", "group", "tasks", "completed tasks", "language")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Student", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.create_field, enumerate(self.fields)))
        self.frame.pack()

    def create_field(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def load_details(self, student: Student):
        values = (student.first_name, student.second_name, student.third_name, student.course,
                  student.group, student.tasks, student.completed_tasks, student.language)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def get_student(self) -> Student:
        values = [e.get() for e in self.entries]
        params = list(values)
        params.insert(0, 0)
        try:
            params[4] = int(params[4])
            params[6] = int(params[6])
            params[7] = int(params[7])
            student = Student(*params)
            if self._is_not_valid(student):
                raise ValueError('Not correct data')
            return student
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    @staticmethod
    def _is_not_valid(student: Student) -> bool:
        return (student.completed_tasks < 0 or student.completed_tasks > student.tasks
                or student.language not in ['Java', 'cxx', 'Python'])
