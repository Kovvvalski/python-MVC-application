import tkinter as tk
from view.students_tree import StudentsTree


class AlternativeViewWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.TOP)

        self.title("Students tree")

        self.tree = StudentsTree(self)
        self.tree.pack(padx=10, pady=10, side=tk.TOP)
