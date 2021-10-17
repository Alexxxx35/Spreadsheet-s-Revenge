import tkinter as tk
from winsound import *
import json
from components.destroyer import destroyer
from spreadsheet.file_generator import spreadsheet_generator
from tkinter import filedialog


class data_generation_page:
    counter = 0

    def __init__(self, root: tk.Tk) -> None:
        PlaySound("sounds/click.wav", SND_FILENAME)
        self.root = root
        destroyer(self.root)
        self.generator_menu_label = tk.Label(
            root, text="Spreadsheet Cleaner File Generator")
        self.generator_menu_label.place(x=180)
        self.number_of_row_label = tk.Label(
            root, text="How many rows must include the false document:")
        self.number_of_row_label.grid(row=1, column=0, pady=50, padx=10)
        self.number_of_rows = tk.Entry(
            root)
        self.number_of_rows.grid(row=1, column=1, padx=10)

        self.number_of_col_label = tk.Label(
            root, text="How many cols must include the false document:")
        self.number_of_col_label.grid(row=2, column=0, pady=50, padx=10)
        self.number_of_cols = tk.Entry(
            root)
        self.number_of_cols.grid(row=2, column=1, padx=10)

        self.generation_next_button = tk.Button(
            root, text="next>", width=15)
        self.generation_next_button.place(x=400, y=320)
        self.generation_next_button.config(
            state="disabled", fg='grey', command=self.generation_next)
        self.number_of_rows.bind("<Return>", self.generation_row_clicker)
        self.number_of_cols.bind("<Return>", self.generation_col_clicker)

    def generation_row_clicker(self, callback):
        self.counter += 1
        self.number_of_rows_value = int(self.number_of_rows.get())
        self.number_of_rows.destroy()
        if self.counter == 2:
            self.generation_next_button.config(state="active", fg="black")
        self.number_of_rows = tk.Entry(
            self.root)
        self.number_of_rows.grid(row=1, column=1, padx=10)
        self.number_of_rows.insert(0, self.number_of_rows_value)
        self.number_of_rows.config(state='readonly', fg='grey')

    def generation_col_clicker(self, callback):
        self.counter += 1
        self.number_of_cols_value = int(self.number_of_cols.get())
        self.number_of_cols.destroy()
        if self.counter == 2:
            self.generation_next_button.config(state="active", fg="black")
        self.number_of_cols = tk.Entry(
            self.root)
        self.number_of_cols.grid(row=2, column=1, padx=10)
        self.number_of_cols.insert(0, self.number_of_cols_value)
        self.number_of_cols.config(state='readonly', fg='grey')

    def generation_next(self):
        PlaySound("sounds/click.wav", SND_FILENAME)
        self.entries = []
        col = 0
        destroyer(self.root)
        self.data_generator = spreadsheet_generator(
            int(self.number_of_cols_value))
        self.csv_object = self.data_generator.fake_data()
        data_dict = self.data_generator.profile
        data_dict_keys = list(data_dict.keys())
        print(data_dict_keys)
        for x in range(self.number_of_cols_value):
            entry = "entry{}".format(x)
            self.entries.append(entry)
        i = 1
        x = 0
        for str in self.entries:
            if i % 8 == 0:
                col += 2
                i = 1
            self.row_label = tk.Label(
                self.root, text="field:")
            self.row_label.grid(row=i, column=col, pady=20)
            str = tk.Entry(self.root)
            str.insert(0, data_dict_keys[x])
            str.config(state='readonly', fg='grey')
            str.grid(row=i, column=col+1, padx=10)
            i += 1
            x += 1
        self.generation_next_button = tk.Button(
            self.root, text="generate the file", width=15)
        self.generation_next_button.place(x=400, y=320)
        self.generation_next_button.config(
            command=self.generate_file)

    def generate_file(self):
        PlaySound("sounds/click.wav", SND_FILENAME)
        destroyer(self.root)
        self.generator_menu_label = tk.Label(
            self.root, text="Spreadsheet Cleaner File Generator")
        self.generator_menu_label.place(x=180)

        self.path_label = tk.Label(
            self.root, text="Select the path to store the document:")
        self.path_label.grid(row=1, column=0, pady=100, padx=10)
        self.path_entry = tk.Entry(
            self.root)
        self.path_entry.config(state='readonly', fg='grey')
        self.path_entry.grid(row=1, column=1, padx=10)
        self.path_button = tk.Button(
            self.root, text="path", width=5, command=self.fill_entry_path)
        self.path_button.grid(row=1, column=2, sticky='w')

    def fill_entry_path(self):
        PlaySound("sounds/click.wav", SND_FILENAME)
        self.directory = filedialog.askdirectory(
            parent=self.root, initialdir="C:/Users/PC/", title="Please select a directory")
        print(self.directory)
        self.path_entry.config(state="normal", fg="black")
        self.path_entry.insert(0, self.directory)

        self.quit_button = tk.Button(
            self.root, text="OK", width=15)
        self.quit_button.place(x=400, y=280)
        self.quit_button.config(
            command=self.generation_launched)

        self.quit_button = tk.Button(
            self.root, text="Exit", width=15)
        self.quit_button.place(x=400, y=320)
        self.quit_button.config(
            command=quit)

    def generation_launched(self):
        PlaySound("sounds/click.wav", SND_FILENAME)
        self.data_generator.csv_builder(
            json.dumps(self.csv_object), self.directory, False)

    def quit(self):
        PlaySound("sounds/click.wav", SND_FILENAME)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.destroy()
