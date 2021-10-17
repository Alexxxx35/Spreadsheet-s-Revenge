import tkinter as tk


class destroyer:
    def __init__(self, tk: tk.Tk, *args) -> None:
        # self.l=[]
        # self.l.append(args)
        # for e in self.l:
        #     e.destroy()
        for widget in tk.winfo_children():
            widget.destroy()
