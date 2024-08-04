import tkinter as tk
from view.students_list import StudentsList


class FindWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.TOP)

        self.condition_label = tk.Label(self.frame, text="Select condition:")
        self.condition_label.pack(side=tk.LEFT)

        self.title("Find dialog")

        self.condition_var = tk.StringVar()
        self.condition_var.set("By name")
        self.condition_menu = tk.OptionMenu(
            self.frame, self.condition_var, "By name", "By language", "By completed tasks", "By not completed tasks"
        )

        self.condition_menu.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.frame, text="Search")
        self.search_button.pack(side=tk.LEFT)

        self.list = StudentsList(self)
        self.list.pack(padx=10, pady=10, side=tk.TOP)
