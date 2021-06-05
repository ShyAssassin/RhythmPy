try:
    import tkinter as tk
    from tkinter import Button, Label, filedialog, messagebox, ttk
except (ImportError, ModuleNotFoundError):
    import Tkinter as tk
    from Tkinter import ttk, Button, Label, messagebox, filedialog

from Core import (
    Gui,
)


BUTTON_PADX = 4
BUTTON_PADY = 8
BUTTON_PADX_ITALIC = 9
BUTTON_PADY_ITALIC = 11
BUTTON_FONT = ("Yu Gothic UI", 14)
BUTTON_FONT_LARGE = ("Yu Gothic UI", 15)
BUTTON_FONT_BOLD = ("Yu Gothic UI", 14, "bold")
BUTTON_FONT_ITALIC = ("Yu Gothic UI", 13, "italic")
BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2
BUTTON_STYLE = "solid"  # flat, groove, raised, ridge, solid, sunken


# used for all UI elements including button functions!
class Settings(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("500x500")
        self.master.title(u"RhythmPy")
        # IDK
        self.entry = tk.Entry(
            self.master,
            font=("Yu Gothic UI", 32, "bold"),
            bg="#333333",
            fg="#fffafa",
            justify="right",
            relief="flat",
        )
        self.Create_Widgets()

    def Create_Widgets(self):
        pass


def Run():
    try:
        root = tk.Tk()
        root.config(bg="#333333")
        root.resizable(width=False, height=False)
        root.wait_visibility()
        root.attributes("-alpha", 0.965)
        Style = ttk.Style(root)
        Style.configure("TP.TFrame", background="snow")
        App = Settings()
        Gui.CenterWin(root)
        App.mainloop()
    except Exception:
        pass


if __name__ == "__main__":
    Run()
