try:
    from tkinter import messagebox
except ImportError:
    from Tkinter import messagebox

try:
    from .Logger import Logger
except ImportError:
    from Logger import Logger

import sys

# used to close application globally
def CloseGlobal(master):
    if master == None or master == '':
        sys.exit()
        exit()
    else:
        root = master
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            loggerinit = Logger()
            logger = loggerinit.StartLogger(name=__name__)
            root.destroy()
            logger.info('Quiting!')
            sys.exit()
            exit()