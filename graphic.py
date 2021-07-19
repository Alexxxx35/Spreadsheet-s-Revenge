import tkinter as tk
from tkinter import font, Menu
import os


class app_window:
    def __init__(self, title: str, *window_size: tuple) -> None:
        self.root = tk.Tk()
        print(font.families())
        self.root.iconbitmap(os.path.join("images", "spreadsheet.ico"))
        #self.menubar = Menu(self.root, background="blue", fg="grey")
        # self.root.config(menu=self.menubar)
        if not window_size:
            w = 800  # width for the Tk root
            h = 650  # height for the Tk root
        else:
            w = window_size[0][0]
            h = window_size[0][1]
        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # self.font = tkinter.font.Font(family=font)
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

    def data_generation_page(self):
        self.menu_label.destroy()
        self.data_generation_button.destroy()
        self.generator_menu_label = tk.Label(
            self.root, text="Spreadsheet Cleaner File Generator")
        self.generator_menu_label.grid(row=0, column=1)


menu_window = app_window("Spreadsheet Cleaner", (600, 400))
menu_window.menu()
menu_window.main()
