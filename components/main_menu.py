import tkinter as tk
from components.data_generator_menu import data_generation_page

class main_menu:
    def __init__(self,root:tk.Tk) -> None:
        self.menu_label = tk.Label(
            root, text=" Welcome to Spreadsheet Cleaner.\n Choose an action:")
        self.menu_label.grid(row=0, column=1)
        self.data_generation_button = tk.Button(text="Data generation menu", width=20,
                                                height=2, command=lambda:data_generation_page(root))
        self.data_generation_button.grid(row=1, column=0, padx=10, pady=30)