import tkinter as tk


class DeleteWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Delete window")
        self.geometry("300x300")

        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.TOP)

        self.condition_label = tk.Label(self.frame, text="Select condition:")
        self.condition_label.pack(side=tk.LEFT)

        self.condition_var = tk.StringVar()
        self.condition_var.set("By name")
        self.condition_menu = tk.OptionMenu(
            self.frame, self.condition_var, "By name", "By language", "By completed tasks", "By not completed tasks"
        )
        self.condition_menu.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.frame, text="Delete")
        self.delete_button.pack(side=tk.LEFT)
