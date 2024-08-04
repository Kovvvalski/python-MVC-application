import tkinter as tk
from tkinter import ttk
from model.entity.student import Student


class StudentsList(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.tree = ttk.Treeview(self, columns=("first_name", "second_name", "third_name", "course", "group",
                                                "tasks", "completed_tasks", "language"), show="headings")

        self.tree.column("first_name", width=80)
        self.tree.column("second_name", width=80)
        self.tree.column("third_name", width=80)
        self.tree.column("course", width=50)
        self.tree.column("group", width=50)
        self.tree.column("tasks", width=40)
        self.tree.column("completed_tasks", width=100)
        self.tree.column("language", width=70)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tree.heading("first_name", text="First name", anchor="w")
        self.tree.heading("second_name", text="Second name", anchor="w")
        self.tree.heading("third_name", text="Third name", anchor="w")
        self.tree.heading("course", text="Course", anchor="w")
        self.tree.heading("group", text="Group", anchor="w")
        self.tree.heading("tasks", text="Tasks", anchor="w")
        self.tree.heading("completed_tasks", text="Completed tasks", anchor="w")
        self.tree.heading("language", text="Language", anchor="w")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def populate_tree(self, students: list[Student]):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for student in students:
            self.tree.insert("", "end", values=(student.first_name, student.second_name,
                                                student.third_name, student.course, student.group, student.tasks,
                                                student.completed_tasks, student.language))
