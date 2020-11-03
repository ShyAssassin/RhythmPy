import tkinter as tk
from tkinter import ttk, Entry

class Settings:
    def __init__(self):
        # this is so bad
        self.masters = tk.Tk()
        canvas = tk.Canvas(self.masters)
        self.masters.geometry('500x500')
        self.masters.title(u'Settings')
        # creates widgets
        self.Create_Widgets()
        self.masters.config(bg='#333333')
        self.masters.resizable(width=False, height=False)
        self.masters.attributes("-alpha",0.965)
        # not sure what this days tbh
        ttk.Style().configure("TP.TFrame", background="snow")
        self.masters.mainloop()

    def Create_Widgets(self):
        pass

    def Run(self):
        self.masters.mainloop()


if __name__ == "__main__":
    Settings().Run()