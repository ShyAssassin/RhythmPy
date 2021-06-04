from tkinter import messagebox
from .Logger import Logger
import sys


# used to close application globally
def CloseGlobal(master, running=None):
    """Closes the app"""
    if running in [False, None]:
        loggerinit = Logger()
        logger = loggerinit.StartLogger(name=__name__)
        # checks for tkinter window
        if master == None or master == "":
            logger.info("Quiting!\n")
            sys.exit()
            exit()
            sys.exit()
        else:
            root = master
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                logger.info("Quiting!\n")
                sys.exit()
                exit()
                sys.exit()
    else:
        messagebox.showwarning(
            "Bot is running", "The bot is currently running exit it before quiting."
        )
