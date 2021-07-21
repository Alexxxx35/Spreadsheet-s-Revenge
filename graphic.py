import tkinter as tk
import json
from tkinter import StringVar, font, Menu, filedialog
import os
from tkinter.constants import CENTER, DISABLED, SE
import file_generator


class app_window:
    def __init__(self, title: str, *window_size: tuple) -> None:
        self.counter = 0
        self.root = tk.Tk()
       # print(font.families())
        self.root.iconbitmap(os.path.join("images", "spreadsheet.ico"))

        # self.menubar = Menu(self.root, background="blue", fg="grey")
        # self.root.config(menu=self.menubar)

        if not window_size:
            w = 800  # width for the Tk root
            h = 650  # height for the Tk root
        else:
            w = window_size[0][0]
            h = window_size[0][1]

        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Javanese Text",
                                   size=10,
                                   weight=font.NORMAL)
        self.root.title(title)

    def menu(self):
        self.menu_label = tk.Label(
            self.root, text=" Welcome to Spreadsheet Cleaner.\n Choose an action:")
        self.menu_label.grid(row=0, column=1)
        self.data_generation_button = tk.Button(text="Data generation menu", width=20,
                                                height=2, command=lambda: self.data_generation_page())
        self.data_generation_button.grid(row=1, column=0, padx=10, pady=30)

    def main(self):
        self.root.mainloop()

    def quit(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.destroy()

    def clean_entry(self):
        self.path_entry.delete()

    def generation_launched(self):
        self.data_generator.csv_builder(
            json.dumps(self.csv_object), self.directory, False)

    def fill_entry_path(self):
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
            command=self.quit)

    def generate_file(self):
        for widget in self.root.winfo_children():
            widget.destroy()
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

    def generation_next(self):
        self.entries = []
        col = 0
        self.number_of_rows.destroy()
        self.number_of_row_label.destroy()
        self.number_of_cols.destroy()
        self.number_of_col_label.destroy()
        self.generation_next_button.destroy()
        self.data_generator = file_generator.data(
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

    def generation_row_clicker(self, callback):
        self.counter += 1
        self.number_of_rows_value = int(self.number_of_rows.get())
        self.number_of_rows.destroy()
        if self.counter == 2:
            self.generation_next_button.config(state="active", fg="black")
        # self.number_of_row_label.destroy()
        # self.number_of_row_label = tk.Label(
        #    self.root, text="How many rows must include the false document:")
        #self.number_of_row_label.grid(row=1, column=0, pady=50, padx=10)
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
        # self.number_of_col_label.destroy()
        # self.number_of_col_label = tk.Label(
        #    self.root, text="How many cols must include the false document:")
        #self.number_of_col_label.grid(row=2, column=0, pady=50, padx=10)
        self.number_of_cols = tk.Entry(
            self.root)
        self.number_of_cols.grid(row=2, column=1, padx=10)
        self.number_of_cols.insert(0, self.number_of_cols_value)
        self.number_of_cols.config(state='readonly', fg='grey')

    def data_generation_page(self):
        self.menu_label.destroy()
        self.data_generation_button.destroy()
        self.generator_menu_label = tk.Label(
            self.root, text="Spreadsheet Cleaner File Generator")
        self.generator_menu_label.place(x=180)
        self.number_of_row_label = tk.Label(
            self.root, text="How many rows must include the false document:")
        self.number_of_row_label.grid(row=1, column=0, pady=50, padx=10)
        self.number_of_rows = tk.Entry(
            self.root)
        self.number_of_rows.grid(row=1, column=1, padx=10)

        self.number_of_col_label = tk.Label(
            self.root, text="How many cols must include the false document:")
        self.number_of_col_label.grid(row=2, column=0, pady=50, padx=10)
        self.number_of_cols = tk.Entry(
            self.root)
        self.number_of_cols.grid(row=2, column=1, padx=10)

        self.generation_next_button = tk.Button(
            self.root, text="next>", width=15)
        self.generation_next_button.place(x=400, y=320)
        self.generation_next_button.config(
            state="disabled", fg='grey', command=self.generation_next)
        self.number_of_rows.bind("<Return>", self.generation_row_clicker)
        self.number_of_cols.bind("<Return>", self.generation_col_clicker)


menu_window = app_window("Spreadsheet Cleaner", (600, 400))
menu_window.menu()
menu_window.main()
