try:
    import tkinter as tk
    from tkinter import ttk, Button, PhotoImage, Label
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk, Button, PhotoImage, Label

from PIL import Image, ImageTk
from os import path
import os
import sys
import json

# more retarded
try:
    from .Modules import ResizeImage, logger, IsProcessRunning
    from .Settings import Settings
except ImportError:
    from Modules import ResizeImage, logger, IsProcessRunning
    from Settings import Settings

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

Defualt_Config = {
    "Version": "",
    "Osu4K":{
        "Window Name": "",
        "Collum1Pos": "",
        "Collum2Pos": "",
        "Collum3Pos": "",
        "Collum4Pos": ""
    },
    "Quaver4K":{
        "Window Name": "", 
        "Collum1Pos": "",
        "Collum2Pos": "",
        "Collum3Pos": "",
        "Collum4Pos": ""
    }
}

# stuff that is needed to run
class Functions:
    def __init__(self):
        logger.info(msg='started')
        PACKAGE_PARENT = '..'
        SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
        sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

    # If Config File exists
    def ConfigExists(self):
        if path.exists('Config.json') == False:
            print('Config file is missing, creating now...')
            logger.warning('Config file missing, creating now')
            # writes config to file
            with open('Config.json', 'w+') as json_file:
                json.dump(Defualt_Config, json_file, indent=4)
                logger.info('defualt config writen to file')

    # checks if process is running
    def Process(self):
        # using global to stop me from having a mental break down dealing with retuns
        global Game
        if(IsProcessRunning('Osu')):
            Game = 'Osu'
        elif(IsProcessRunning('Quaver')):
            Game = 'Qauver'
        else:
            print(' cant find the running Process\n Please select it manually\n Osu or Quaver ')
            GameInput = input()
            if GameInput in ('Osu', 'OSU', 'osu'):
                Game = 'Osu'
            elif GameInput in ('Quaver', 'QUAVER' 'quaver'):
                Game = 'Quaver'
            else:
                logger.critical('what the actual fuck')

# ============================================================================================================

# this creates the ui elements
class Application(tk.Frame):
    def Run(self, master=None):
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
        self.Create_Widgets()

    # stop start command for the button :p
    def Start_Stop(self):
        if(self.Start_StopBTN["text"] == 'START'):
            # starts the program
            print('started')
            # sets text to once started
            self.Start_StopBTN.configure(text="STOP")
        elif(self.Start_StopBTN["text"] == 'STOP'):
            # stops program
            print('stopped')
            # sets text once stopped
            self.Start_StopBTN.configure(text='START')

    # used for moving window when overidedirect() is active
    def SaveLastClickPos(self, event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y


    def Dragging(self, event):
        x, y = event.x - lastClickX + self.master.winfo_x(), event.y - lastClickY + self.master.winfo_y()
        self.master.geometry("+%s+%s" % (x , y))
    #=======================================================================================
    
    '''
    Button Example:
        Button(self.master, text='TEXT', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE)
    Image Button Example:
        self.Image = ResizeImage(100, 100, "UI-Media\icon-gear.png")
        self.Image = ImageTk.PhotoImage(self.Image)
        Button(image = self.Image, relief=BUTTON_STYLE, bg='#333333', fg='#fffafa').pack()
    '''
    def Create_Widgets(self):
        #Widgets
        # Settings Button
        self.SettingsIcon = ResizeImage(80, 80, "UI-Media\icon-gear.png")
        self.SettingsIcon = ImageTk.PhotoImage(self.SettingsIcon)
        self.SettingsBTN = Button(
            self.master,
            image = self.SettingsIcon, 
            relief = 'flat', 
            bg = '#333333', 
            fg = '#fffafa', 
            padx = BUTTON_PADX, 
            pady = BUTTON_PADY, 
            borderwidth = 0,
            activebackground = '#363535',
            command=lambda: Settings()
        )
        self.SettingsBTN.place(x=418, y=568)

        # Start / Stop Button
        self.Start_StopBTN = Button(self.master, 
        text = 'START', 
        font = BUTTON_FONT_BOLD, 
        width = BUTTON_WIDTH, 
        height = BUTTON_HEIGHT, 
        bg = '#333333', 
        fg = '#fffafa', 
        relief = BUTTON_STYLE,
        command = self.Start_Stop
        )
        self.Start_StopBTN.place(x=200, y=250)
        #=====================================================================================

class Run:
    def __init__(self):
        root = tk.Tk()
        root.config(bg='#333333')
        root.resizable(width=False, height=False)
        root.attributes("-alpha",0.965)
        ttk.Style().configure("TP.TFrame", background="snow")
        root.bind('<Button-1>', Application().SaveLastClickPos)
        root.bind('<B1-Motion>', Application().Dragging)
        # root.overrideredirect(1)
        app = Application()
        app.Run()
        app.mainloop()

if __name__ == "__main__":
    Run()


