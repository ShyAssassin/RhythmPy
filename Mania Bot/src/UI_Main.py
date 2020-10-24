import tkinter as tk
from tkinter import ttk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label
from PIL import Image, ImageTk
# more retarded
try:
    from .Modules import ResizeImage
except:
    from Modules import ResizeImage

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
BUTTON_STYLE = "flat" # flat, groove, raised, ridge, solid, sunken

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry('500x650')
        self.master.title(u'Mania Bot')

        self.entry = tk.Entry(
            self.master,
            font=("Yu Gothic UI", 32, "bold"),
            bg='#333333',
            fg='#fffafa',
            justify='right',
            relief="flat"
            )

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)


        self.create_widgets()

    '''
    Button Example:
        tk.Button(self.master, text='TEXT', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE)
    Image Button Example:
        self.Image = ResizeImage(100, 100, "UI-Media\icon-gear.png")
        self.Image = ImageTk.PhotoImage(self.Image)
        Button(image = self.Image, relief=BUTTON_STYLE, bg='#333333', fg='#fffafa').pack()
    '''
    def create_widgets(self):
        # menu_bar
        self.menu_bar.add_cascade(label='Options')
        #====================================================================================

        #Widgets
        self.Icon = ResizeImage(100, 100, "UI-Media\icon-gear.png")
        self.Icon = ImageTk.PhotoImage(self.Icon)
        Button(image = self.Icon, relief=BUTTON_STYLE, bg='#333333', fg='#fffafa', padx=BUTTON_PADX, pady=BUTTON_PADY).pack()
        #=====================================================================================

class run:
    def __init__(self):
        root = tk.Tk()
        root.config(bg='#333333')
        root.resizable(width=False, height=False)
        root.attributes("-alpha",0.945)
        ttk.Style().configure("TP.TFrame", background="snow")
        app = Application(master=root)
        app.mainloop()

if __name__ == "__main__":
    run()


