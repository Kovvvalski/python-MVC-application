import tkinter as tk
from view.student_form import StudentForm


class NewStudent(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.student = None
        self.form = StudentForm(self)
        self.btn_add = tk.Button(self, text="Add", command=self.confirm)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirm(self):
        self.student = self.form.get_student()
        if self.student:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.student
