try:
    from tkinter import messagebox
except ImportError:
    from Tkinter import messagebox

import sys

# used to close application globally
def CloseGlobal(master):
    if master == None or master == '':
        sys.exit()
        exit()
    else:
        root = master
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            print('Quiting!')
            sys.exit()
            exit()