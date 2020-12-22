import tkinter as tk
from tkinter import ttk, Entry

try:
    from .Modules import CenterWin
except ImportError:
    from Modules import CenterWin

# this isnt in modules because it is related to ui and not "back end"
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
        # not sure what this does tbh
        ttk.Style().configure("TP.TFrame", background="snow") 
        CenterWin(self.masters)
        self.masters.mainloop()

    def Create_Widgets(self):
        pass

if __name__ == "__main__":
    Settings()