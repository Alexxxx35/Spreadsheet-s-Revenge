import tkinter as tk
import tkinter.font
#from file_generator import *


class app_window:
    def __init__(self, title: str, font: str, window_size: tuple) -> None:
        self.root = tk.Tk()
        self.font = tkinter.font.Font(family=font)
        self.root.title(title)
        self.root.geometry(str(window_size[0])+'x'+str(window_size[1]))

    def menu(self):
        label = tk.Label(
            self.root, text=" Welcolme to Spreadsheet's Revenge. Clean up your data like a noob!")
        label.pack()

    def main(self):
        self.root.mainloop()


menu_window = app_window("xfileFormatter", "Helvetica", (600, 400))
menu_window.menu()
menu_window.main()
