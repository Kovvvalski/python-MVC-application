import tkinter as tk
from tkinter import ttk
from tkinter import *
from model.entity.student import Student


class StudentsTree(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.tree = ttk.Treeview(self, show="tree")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def populate_tree(self, students: list[Student]):
        self.tree.insert("", END, iid=1, text="Students", open=True)
        for student in students:
            student_node = self.tree.insert("", "end", text=student.first_name)

            self.tree.insert(student_node, "end", text="First Name - " + student.first_name)
            self.tree.insert(student_node, "end", text="Second Name - " + student.second_name)
            self.tree.insert(student_node, "end", text="Third Name - " + student.third_name)
            self.tree.insert(student_node, "end", text="Course - " + str(student.course))
            self.tree.insert(student_node, "end", text="Group - " + student.group)
            self.tree.insert(student_node, "end", text="Tasks - " + str(student.tasks))
            self.tree.insert(student_node, "end", text="Completed Tasks - " + str(student.completed_tasks))
            self.tree.insert(student_node, "end", text="Language - " + student.language)
