try:
    import tkinter as tk
    from tkinter import ttk, Button, PhotoImage, Label, messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk, Button, PhotoImage, Label, messagebox

from PIL import Image, ImageTk
from os import path
import os
import sys
import json
import time
import logging
import threading

# more retarded
try:
    from .Modules import ResizeImage, IsProcessRunning, Windowcapture, UpdateConfig, FirstRun
    from .Settings import Settings
except ImportError:
    from Modules import ResizeImage, IsProcessRunning, WindowCapture, UpdateConfig, FirstRun
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

# needs to be updated when new key is used
Defualt_Config_Osu4K = {
    "Collums": "4",
    "Window Name": "",
    "Collum1Pos": "",
    "Collum2Pos": "",
    "Collum3Pos": "",
    "Collum4Pos": ""
}

Defualt_Config_Quaver4K = {
    "Collums": "4",
    "Window Name": "",
    "Collum1Pos": "",
    "Collum2Pos": "",
    "Collum3Pos": "",
    "Collum4Pos": ""
}

Defualt_Settings = {
    "Version": "1",
    "Debug": "False",
    "FirstRun": "True",
    "MultiConfig": "False",
}

# used for non UI related things
class Functions:
    def __init__(self):
        # gets logger
        self.logger = logging.getLogger(__name__)
        # sets logger level
        self.logger.setLevel(logging.DEBUG)
        # define file handler and set formatter
        self.LoggingFile = logging.FileHandler('app.log')
        self.Formatter = logging.Formatter('%(name)s, %(lineno)d || %(asctime)s :: %(levelname)s :: %(message)s')
        self.LoggingFile.setFormatter(self.Formatter)
        # add file handler to logger
        self.logger.addHandler(self.LoggingFile)

        PACKAGE_PARENT = '..'
        SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
        sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

    '''
    imma be honest 
    you need to close the below functions so it dont look like shit
    '''
    # checks if process is running and selecting game with UI      
    def Process(self):
        # using global to stop me from having a mental break down dealing with retuns
        global Game
        if(IsProcessRunning('Osu')):
            Game = 'Osu'
        elif(IsProcessRunning('Quaver')):
            Game = 'Qauver'
        else:
            print('cant find the running Process\nPlease select it manually')

            # just adding a UI for selecting game
            self.masters = tk.Tk()
            canvas = tk.Canvas(self.masters)
            self.masters.geometry('400x550')
            self.masters.title(u'Select Game!')

            # creates widgets
            Label(
                self.masters,
                font = BUTTON_FONT_BOLD,
                bg = '#333333',
                fg = '#fffafa',
                text='Could not a find running game!'
                ).pack()

            Label(
                self.masters,
                font = BUTTON_FONT_BOLD,
                bg = '#333333',
                fg = '#fffafa',
                text='Please select a game manually!'
                ).place(x=63, y=185)

            self.OsuBTN = Button(
                self.masters, 
                text = 'Osu', 
                font = BUTTON_FONT_BOLD, 
                width = BUTTON_WIDTH, 
                height = BUTTON_HEIGHT, 
                bg = '#333333', 
                fg = '#fffafa', 
                relief = BUTTON_STYLE,
                command=lambda: self.SetGame(self.masters, 'Osu')
                )
            self.OsuBTN.place(x=215, y=225)

            self.QuaverBTN = Button(
                self.masters, 
                text = 'Quaver', 
                font = BUTTON_FONT_BOLD, 
                width = BUTTON_WIDTH, 
                height = BUTTON_HEIGHT, 
                bg = '#333333', 
                fg = '#fffafa', 
                relief = BUTTON_STYLE,
                command=lambda: self.SetGame(self.masters, 'Quaver')
                )
            self.QuaverBTN.place(x=65, y=225)

            self.masters.config(bg='#333333')
            self.masters.resizable(width=False, height=False)
            self.masters.attributes("-alpha",0.965)
            # not sure what this does tbh
            ttk.Style().configure("TP.TFrame", background="snow")
            self.masters.protocol("WM_DELETE_WINDOW", lambda: self.CloseGlobal(self.masters))
            # runs window
            self.masters.mainloop()
        # ====================================================================================================================

    # change game during runtime with UI            
    def ChangeGame(self):
            # just adding a UI for selecting game
            self.masters = tk.Tk()
            canvas = tk.Canvas(self.masters)
            self.masters.geometry('400x550')
            self.masters.title(u'Select Game!')

            # creates widgets
            Label(
                self.masters,
                font = BUTTON_FONT_BOLD,
                bg = '#333333',
                fg = '#fffafa',
                text='Please select a game!'
                ).place(x=63, y=185)

            self.OsuBTN = Button(
                self.masters, 
                text = 'Osu', 
                font = BUTTON_FONT_BOLD, 
                width = BUTTON_WIDTH, 
                height = BUTTON_HEIGHT, 
                bg = '#333333', 
                fg = '#fffafa', 
                relief = BUTTON_STYLE,
                command=lambda: self.SetGame(self.masters, 'Osu')
                )
            self.OsuBTN.place(x=215, y=225)

            self.QuaverBTN = Button(
                self.masters, 
                text = 'Quaver', 
                font = BUTTON_FONT_BOLD, 
                width = BUTTON_WIDTH, 
                height = BUTTON_HEIGHT, 
                bg = '#333333', 
                fg = '#fffafa', 
                relief = BUTTON_STYLE,
                command=lambda: self.SetGame(self.masters, 'Quaver')
                )
            self.QuaverBTN.place(x=65, y=225)

            self.masters.config(bg='#333333')
            self.masters.resizable(width=False, height=False)
            self.masters.attributes("-alpha",0.965)
            # not sure what this does tbh
            ttk.Style().configure("TP.TFrame", background="snow")
            # runs window
            self.masters.mainloop()
        # ====================================================================================================================

    # used to close application globally
    def CloseGlobal(self, master):
        if master == None or master == '':
            exit()
        else:
            self.root = master
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                print('Quiting!')
                try:
                    exit()
                except:
                    sys.exit()

    # used to set game during run time
    def SetGame(self, master, game):
        global Game
        Game = game
        self.Game = game
        print('changed game to ' + Game)
        # used for closing window if there is one
        self.SetGameMaster = master
        if self.SetGameMaster == None or self.SetGameMaster == False or self.SetGameMaster == "" or self.SetGameMaster == " ":
            pass
        else:
            # does not need to close gloabal for this one
            # just the current window
            self.SetGameMaster.destroy()
        
    # If Config Folder exists
    def ConfigFolderExists(self):
        if path.exists('Config') == False:
            print('Config folder is missing, creating now...')
            self.logger.warning('Config file missing, creating now')
            try:
                os.mkdir('Config')
                print('Created config dir')
                self.logger.info('Created config dir')
            except:
                print('could not create Config dir')
                self.logger.critical('could not create Config dir')
                exit()
                sys.exit()
            return False
        else:
            return True

    # creates defualt config files
    def CreateConfigFiles(self):
        # writes settings
        if path.exists(r"Config\Settings.json"):
            pass
        else:
            with open(r"Config\Settings.json", "w+") as json_file:
                json.dump(Defualt_Settings, json_file, indent=4)
                print('created Settings.json')
                self.logger.info('created Settings.json')

        # writes Osu
        if path.exists(r"Config\Osu4K.json"):
            pass
        else:
            with open(r"Config\Osu4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Osu4K, json_file, indent=4)
                print('created Osu4K.json')
                self.logger.info('created Osu4K.json')

        # writes quaver
        if path.exists(r"Config\Quaver4K.json"):
            pass
        else:
            with open(r"Config\Quaver4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Quaver4K, json_file, indent=4)
                print('created Quaver4K.json')
                self.logger.info('created Quaver4K.json')
# ============================================================================================================

class Bot:
    def __init__(self, Game, Running):
        self.Running = Running
        # self.Gamemode = Gamemode
        self.Game = Game

    def ManiaStart(self):
        if Game == 'Osu':
            # loads Config file
            pass
        elif Game == 'Quaver':
            # loads config file
            pass
        # will need to be updated to reflect the name of window found in Config
        Wincap = WindowCapture(None)
        Wincap.start()
        print('Window Capture started')
        while self.Running == True:
            if Wincap.screenshot is None:
                continue
            # used for stopping the stuff
            if Running == False:
                Wincap.stop()
                break

            ScreenCap = Wincap.screenshot
# ============================================================================================================

# used for all UI elements including button functions!
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        # define file handler and set formatter
        self.LoggingFile = logging.FileHandler('app.log')
        self.Formatter = logging.Formatter('%(name)s, %(lineno)d || %(asctime)s :: %(levelname)s :: %(message)s')
        self.LoggingFile.setFormatter(self.Formatter)
        # add file handler to logger
        self.logger.addHandler(self.LoggingFile)

        self.master.geometry('500x650')
        self.master.title(u'RhythmPy')
        # IDK
        self.entry = tk.Entry(
            self.master,
            font=("Yu Gothic UI", 32, "bold"),
            bg='#333333',
            fg='#fffafa',
            justify='right',
            relief="flat"
            )
        # print(Game)
        self.Create_Widgets()
        # ===========================================================================================================

    # stop start command for the button :p
    def StartStop(self):
        '''
        i am using threads because if i dont it will break tkinter's main loop
        and the UI and become unresponsive
        '''
        global Running
        if(self.Start_StopBTN["text"] == 'START'):
            Running = True
            # give current game and if it is running
            bot = Bot(Game, Running)
            # will be used when i decide to add a way to change gamemode
            # also for osu base game support
            if Game == 'Osu':
                # runs Osu version            
                self.t1 = threading.Thread(target=bot.ManiaStart)
                self.t1.start()
            elif Game == 'Quaver':
                # runs the Quaver version           
                self.t1 = threading.Thread(target=bot.ManiaStart)
                self.t1.start()

            print('started')
            # sets text to once started
            self.Start_StopBTN.configure(text="STOP")
        elif(self.Start_StopBTN["text"] == 'STOP'):
            # stops program
            Running = False
            self.t1.join()
            print('stopped')
            # sets text once stopped
            self.Start_StopBTN.configure(text='START')
        else:
            print('Bruh')
        # ===========================================================================================================

    # will be used Gamemode
    def GameMode(self):
        pass

    # used for moving window when overidedirect(1) is active
    def SaveLastClickPos(self, event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    # used for moving window when overidedirect(1) is active
    def Dragging(self, event):
        x, y = event.x - lastClickX + self.master.winfo_x(), event.y - lastClickY + self.master.winfo_y()
        self.master.geometry("+%s+%s" % (x , y))

    '''
    Button Example:
        Button(self.master, text='TEXT', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE)
    Image Button Example:
        self.Image = ResizeImage(100, 100, "UI-Media\icon-gear.png")
        self.Image = ImageTk.PhotoImage(self.Image)
        Button(image = self.Image, relief=BUTTON_STYLE, bg='#333333', fg='#fffafa').pack()
    '''

    #Widgets
    def Create_Widgets(self):
        # Settings Button
        try:
            try:
                self.SettingsIcon = ResizeImage(82, 82, r"src\UI-Media\icon-gear.png")
            except:
                self.SettingsIcon = ResizeImage(82, 82, r"UI-Media\icon-gear.png")
        except:
            self.logger.critical('can not load or find needed icons')

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
    # ===========================================================================================================
        # used for changing currently loaded config
        # has no use for now will be used for a later feature
        try:
            try:
                self.ChangeConfigIcon = ResizeImage(82, 82, r"src\UI-Media\Config-icon.png")
            except:
                self.ChangeConfigBTN = ResizeImage(82, 82, r"UI-Media\Config-icon.png")
        except:
            self.logger.critical('can not load or find needed icons')

        self.ChangeConfigIcon = ImageTk.PhotoImage(self.ChangeConfigIcon)
        self.ChangeConfigBTN = Button(
            self.master,
            image = self.ChangeConfigIcon,
            relief = 'flat', 
            bg = '#333333', 
            fg = '#fffafa', 
            padx = BUTTON_PADX, 
            pady = BUTTON_PADY, 
            borderwidth = 0,
            activebackground = '#363535',
        )
        # position this!
        # self.ChangeConfigBTN.place()
    # ===========================================================================================================

        # Start / Stop Button
        self.Start_StopBTN = Button(
            self.master, 
            text = 'START', 
            font = BUTTON_FONT_BOLD, 
            width = BUTTON_WIDTH, 
            height = BUTTON_HEIGHT, 
            bg = '#333333', 
            fg = '#fffafa', 
            relief = BUTTON_STYLE,
            command = self.StartStop
        )
        self.Start_StopBTN.place(x=190, y=255)
    # ===========================================================================================================

        self.ChangeGameBTN = Button(
            self.master,
            text = 'Change Game',
            font = BUTTON_FONT_BOLD,
            width = BUTTON_WIDTH,
            height = BUTTON_HEIGHT,
            bg = '#333333', 
            fg = '#fffafa', 
            relief = BUTTON_STYLE,
            command =lambda: Functions().ChangeGame()
        )
        # position this!
        # self.ChangeGameBTN.place(x=100, y=200)
    # ========================================================================================================
# ============================================================================================================

class Run:
    def __init__(self):
        # checks if config exists
        Functions().ConfigFolderExists()
        Functions().CreateConfigFiles()

        # used for checking if the json has all the needed keys
        # not done yet needs to be fixed!
        # UpdateConfig(Defualt_Config)

        # used for first run
        FirstRun().Run()

        # checks for running Games, needs to be run after config checking
        Functions().Process()

        # Main Window Stuff
        root = tk.Tk()        
        root.config(bg='#333333')
        root.resizable(width=False, height=False)
        root.attributes("-alpha",0.965)
        ttk.Style().configure("TP.TFrame", background="snow")
        # binds
        root.bind('<Button-1>', Application().SaveLastClickPos)
        root.bind('<B1-Motion>', Application().Dragging)
        root.protocol("WM_DELETE_WINDOW", lambda: Functions().CloseGlobal(root))
        # root.overrideredirect(1)        
        app = Application()              
        app.mainloop()
# ============================================================================================================

if __name__ == "__main__":
    Run()