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
def CloseGlobal(master, running):
    loggerinit = Logger()
    logger = loggerinit.StartLogger(name=__name__)
    if running in [False, None]:
        if master == None or master == '':
            logger.info('Quiting!')
            sys.exit()
            exit()
        else:
            root = master
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                logger.info('Quiting!')
                sys.exit()
                exit()
    else:
        messagebox.showwarning("Bot is Running", "The Bot is running please close it before exiting")
        logger.warning('user tried to quit app while Bot is Running')