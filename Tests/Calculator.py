import tkinter as tk
from tkinter import ttk

pai = 3.14159265359

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
BUTTON_STYLE = "solid" # flat, groove, raised, ridge, solid, sunken

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry()
        self.master.title(u'test')

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

    def input(self, action):
        self.entry.insert(tk.END, action)

    def reciprocal(self):
        pass

    def square(self):
        pass

    def root(self):
        pass

    def clear_all(self):
        self.entry.delete(0, tk.END)

    def clear_one(self):
        txt = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, txt[:-1])

    def equals(self):
        try:
            self.value = eval(self.entry.get().replace("÷", "/").replace("x", "*").replace("π", str(pai)))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.value)
        except Exception:
            pass

    def create_widgets(self):
        option_menu = tk.Menu(self.menu_bar)
        option_menu.add_command(label='Exit', command=self.master.quit)
        self.menu_bar.add_cascade(label='Option', menu=option_menu)

        self.entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5, ipadx=5, ipady=40)
        self.entry.focus_set()

        tk.Button(self.master, text='%', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input('%')).grid(row=1, column=0)
        tk.Button(self.master, text='π', font=BUTTON_FONT_ITALIC, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX_ITALIC, pady=BUTTON_PADY_ITALIC, relief=BUTTON_STYLE, command=lambda: self.input('π')).grid(row=1, column=1)
        tk.Button(self.master, text='C', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.clear_one()).grid(row=1, column=2)
        tk.Button(self.master, text='AC', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.clear_all()).grid(row=1, column=3)

        tk.Button(self.master, text='1/x', font=BUTTON_FONT_ITALIC, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX_ITALIC, pady=BUTTON_PADY_ITALIC, relief=BUTTON_STYLE, command=lambda: self.reciprocal()).grid(row=2, column=0)
        tk.Button(self.master, text='x²', font=BUTTON_FONT_ITALIC, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX_ITALIC, pady=BUTTON_PADY_ITALIC, relief=BUTTON_STYLE, command=lambda: self.square()).grid(row=2, column=1)
        tk.Button(self.master, text='²√x', font=BUTTON_FONT_ITALIC, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX_ITALIC, pady=BUTTON_PADY_ITALIC, relief=BUTTON_STYLE, command=lambda: self.root()).grid(row=2, column=2)
        tk.Button(self.master, text='÷', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input('÷')).grid(row=2, column=3)

        tk.Button(self.master, text='7', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(7)).grid(row=3, column=0)
        tk.Button(self.master, text='8', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(8)).grid(row=3, column=1)
        tk.Button(self.master, text='9', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(9)).grid(row=3, column=2)
        tk.Button(self.master, text='x', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input('x')).grid(row=3, column=3)

        tk.Button(self.master, text='4', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(4)).grid(row=4, column=0)
        tk.Button(self.master, text='5', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(5)).grid(row=4, column=1)
        tk.Button(self.master, text='6', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(6)).grid(row=4, column=2)
        tk.Button(self.master, text='-', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input('-')).grid(row=4, column=3)

        tk.Button(self.master, text='1', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(1)).grid(row=5, column=0)
        tk.Button(self.master, text='2', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(2)).grid(row=5, column=1)
        tk.Button(self.master, text='3', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(3)).grid(row=5, column=2)
        tk.Button(self.master, text='+', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input('+')).grid(row=5, column=3)

        tk.Button(self.master, text='+/-', font=BUTTON_FONT_ITALIC, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX_ITALIC, pady=BUTTON_PADY_ITALIC, relief=BUTTON_STYLE).grid(row=6, column=0)
        tk.Button(self.master, text='0', font=BUTTON_FONT_BOLD, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input(0)).grid(row=6, column=1)
        tk.Button(self.master, text='.', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#222222', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=lambda: self.input('.')).grid(row=6, column=2)
        tk.Button(self.master, text='=', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#8b4513', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE, command=self.equals).grid(row=6, column=3)


root = tk.Tk()
root.config(bg='#333333')
root.resizable(width=False, height=False)
root.attributes("-alpha",0.96)
ttk.Style().configure("TP.TFrame", background="snow")
app = Application(master=root)
app.mainloop()