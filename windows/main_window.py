from tkinter import font
import os
import tkinter as tk

from components.main_menu import main_menu


class app_window:
    def __init__(self, title: str, *window_size: tuple) -> None:
        self.counter = 0
        self.root = tk.Tk()
        self.root.iconbitmap(os.path.join("images", "spreadsheet.ico"))

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
        main_menu(self.root)
        self.root.mainloop()
