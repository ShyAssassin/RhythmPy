try:
    from tkinter import messagebox
except ImportError:
    from Tkinter import messagebox

try:
    from .Logger import Logger
except ImportError:
    from Logger import Logger

import sys
import time

# used to close application globally
def CloseGlobal(master, running):
    """Closes the app"""
    if running in [False, None]:
        loggerinit = Logger()
        logger = loggerinit.StartLogger(name=__name__)
        if master == None or master == "":
            logger.info("Quiting!\n")
            sys.exit()
            exit()
            sys.exit()
            time.sleep("10")
        else:
            root = master
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                logger.info("Quiting!\n")
                sys.exit()
                exit()
                sys.exit()
                time.sleep("10")
