import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from view.students_list import StudentsList


class StudentsView(tk.Tk):
    standard_pack_args = {
        "side": tk.LEFT,
        "padx": 10,
        "pady": 10,
    }

    def __init__(self):
        super().__init__()
        self.title("Students list")

        # data button frame
        self.data_frame = tk.Frame(self)
        self.data_frame.pack(side=tk.TOP)

        # data list
        self.list = StudentsList(self)
        self.list.pack(padx=10, pady=10, side=tk.TOP)

        self.current_page = tk.Label(self, text="")
        self.current_page.pack()

        # pages button frames
        self.pages_button_frame = tk.Frame(self)
        self.pages_button_frame.pack(side=tk.TOP)

        # buttons
        self.first_page_button = tk.Button(self.pages_button_frame, text="First page")
        self.first_page_button.pack(**self.standard_pack_args)

        self.prev_button = tk.Button(self.pages_button_frame, text="Prev page")
        self.prev_button.pack(**self.standard_pack_args)

        self.next_button = tk.Button(self.pages_button_frame, text="Next page")
        self.next_button.pack(**self.standard_pack_args)

        self.change_rows_button = tk.Button(self.pages_button_frame, text="Change rows")
        self.change_rows_button.pack(**self.standard_pack_args)

        self.last_page_button = tk.Button(self.pages_button_frame, text="Last page")
        self.last_page_button.pack(**self.standard_pack_args)

        self.btn_new = tk.Button(self.data_frame, text="Add student")
        self.btn_new.pack(**self.standard_pack_args)

        self.find_button = tk.Button(self.data_frame, text="Find")
        self.find_button.pack(**self.standard_pack_args)

        self.delete_button = tk.Button(self.data_frame, text="Delete")
        self.delete_button.pack(**self.standard_pack_args)

        self.tree_button = tk.Button(self.data_frame, text="Tree view")
        self.tree_button.pack(**self.standard_pack_args)

        self.change_datasource_label = tk.Label(self.data_frame, text="Change datasource")
        self.change_datasource_label.pack(**self.standard_pack_args)

        self.condition_var = tk.StringVar()
        self.condition_var.set("Database")
        self.datasource_selector = tk.OptionMenu(
            self.data_frame, self.condition_var, "XML", "Database")
        self.datasource_selector.pack(side=tk.LEFT)

        self.confirm_button = tk.Button(self.data_frame, text="Confirm")
        self.confirm_button.pack(**self.standard_pack_args)

    @staticmethod
    def show_change_datasource_dialog() -> str:
        datasource = simpledialog.askstring("New datasource", "Enter new datasource")
        if datasource is not None:
            return datasource

    @staticmethod
    def show_file_not_found_dialog():
        messagebox.showerror("Error", "Not correct filename")

    @staticmethod
    def show_error_dialog(message):
        messagebox.showerror("Error", message)

    @staticmethod
    def show_change_rows_dialog() -> int:
        number = simpledialog.askstring("Number of rows editor", "Enter new number of rows:")
        try:
            number = StudentsView._validate_number(number)
            if 0 >= number:
                raise ValueError
            return number
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid 0 <= number <= 10.")

    @staticmethod
    def show_enter_name_dialog() -> list[str]:
        name = simpledialog.askstring("Find by name", "Enter name:")
        if name is not None:
            names_list = name.split(" ")
            return names_list

    @staticmethod
    def show_enter_language_dialog() -> str:
        name = simpledialog.askstring("Find by language", "Enter language:")
        if name in ["cxx", "Java", "Python"]:
            return name
        messagebox.showerror("Error", "Not correct language")

    @staticmethod
    def show_enter_tasks_dialog() -> int:
        number = simpledialog.askstring("Find tasks", "Enter number:")
        try:
            return StudentsView._validate_number(number)
        except ValueError:
            messagebox.showerror("Error", "Not correct number")

    @staticmethod
    def show_delete_info(rows: int):
        messagebox.showinfo("Delete info", "Deleted rows: " + str(rows))

    @staticmethod
    def _validate_number(number) -> int:
        if number is not None:
            number = int(number)
            return number
