try:
    import tkinter as tk
    from tkinter import Button, Label, filedialog, messagebox, ttk
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk, Button, Label, messagebox, filedialog

import os
import sys
import threading

from PIL import ImageTk

# more retarded imports
try:
    from .Modules import (
        CenterWin,
        CloseGlobal,
        CreateAppdataDir,
        FileManager,
        FirstRun,
        IsProcessRunning,
        Logger,
        ResizeImage,
        WindowCapture,
    )
    from .Settings import Settings

    # from .SplashScreen import SplashScreen
except ImportError:
    from Modules import (
        CenterWin,
        CloseGlobal,
        CreateAppdataDir,
        FileManager,
        FirstRun,
        IsProcessRunning,
        Logger,
        ResizeImage,
        WindowCapture,
    )
    from Settings import Settings

    # from SplashScreen import SplashScreen

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

# used for non main UI related things
class Functions:
    def __init__(self):
        PACKAGE_PARENT = ".."
        SCRIPT_DIR = os.path.dirname(
            os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
        )
        sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

    """
    imma be honest
    you need to close the below functions so it dont look like shit!
    """
    # checks if process is running and selecting game with UI
    def Process(self):
        settings = FileManager().LoadSettings()
        FindRunningProcess = settings["FindRunningProcess"]
        if (
            FindRunningProcess == True
            or FindRunningProcess == "True"
            or FindRunningProcess == "true"
        ):
            # using global to stop me from having a mental break down dealing with retuns
            global Config
            if IsProcessRunning("Osu"):
                Config = "Osu"
            elif IsProcessRunning("Quaver"):
                Config = "Qauver"
            else:
                logger.info("cant find the running Process")

                # just adding a UI for selecting game
                self.masters = tk.Tk()
                canvas = tk.Canvas(self.masters)
                self.masters.geometry("400x550")
                self.masters.title(u"Select Game!")

                # creates widgets
                Label(
                    self.masters,
                    font=BUTTON_FONT_BOLD,
                    bg="#333333",
                    fg="#fffafa",
                    text="Could not a find running game!",
                ).pack()

                Label(
                    self.masters,
                    font=BUTTON_FONT_BOLD,
                    bg="#333333",
                    fg="#fffafa",
                    text="Please select a game manually!",
                ).place(x=63, y=185)

                self.OsuBTN = Button(
                    self.masters,
                    text="Osu",
                    font=BUTTON_FONT_BOLD,
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    bg="#333333",
                    fg="#fffafa",
                    relief=BUTTON_STYLE,
                    command=lambda: self.SetGame(self.masters, "Osu"),
                )
                self.OsuBTN.place(x=215, y=225)

                self.QuaverBTN = Button(
                    self.masters,
                    text="Quaver",
                    font=BUTTON_FONT_BOLD,
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    bg="#333333",
                    fg="#fffafa",
                    relief=BUTTON_STYLE,
                    command=lambda: self.SetGame(self.masters, "Quaver"),
                )
                self.QuaverBTN.place(x=65, y=225)

                self.masters.config(bg="#333333")
                self.masters.resizable(width=False, height=False)
                self.masters.attributes("-alpha", 0.965)
                # not sure what this does tbh
                ttk.Style().configure("TP.TFrame", background="snow")
                self.masters.protocol(
                    "WM_DELETE_WINDOW",
                    lambda: CloseGlobal(self.masters, running=Running),
                )
                CenterWin(self.masters)
                # runs window
                self.masters.mainloop()
        else:
            self.SetGame(master=None, config="Other")
            logger.info("FindRunningProcess is set to False skipping Process Scan")
        # ====================================================================================================================

    # change game during runtime with UI
    def ChangeGame(self):
        # just adding a UI for selecting game
        self.masters = tk.Tk()
        canvas = tk.Canvas(self.masters)
        self.masters.geometry("400x550")
        self.masters.title(u"Select Game!")

        # creates widgets
        Label(
            self.masters,
            font=BUTTON_FONT_BOLD,
            bg="#333333",
            fg="#fffafa",
            text="Please select a game!",
        ).place(x=63, y=185)

        self.OsuBTN = Button(
            self.masters,
            text="Osu",
            font=BUTTON_FONT_BOLD,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg="#333333",
            fg="#fffafa",
            relief=BUTTON_STYLE,
            command=lambda: self.SetGame(self.masters, "Osu"),
        )
        self.OsuBTN.place(x=215, y=225)

        self.QuaverBTN = Button(
            self.masters,
            text="Quaver",
            font=BUTTON_FONT_BOLD,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg="#333333",
            fg="#fffafa",
            relief=BUTTON_STYLE,
            command=lambda: self.SetGame(self.masters, "Quaver"),
        )
        self.QuaverBTN.place(x=65, y=225)

        self.masters.config(bg="#333333")
        self.masters.resizable(width=False, height=False)
        self.masters.attributes("-alpha", 0.965)
        # not sure what this does tbh
        ttk.Style().configure("TP.TFrame", background="snow")
        CenterWin(self.masters)
        # runs window
        self.masters.mainloop()

    # ====================================================================================================================

    # used to set game during run time
    def SetGame(self, master, config):
        global Config
        global ConfigName
        Config = config
        self.Game = config
        logger.info("changed game to " + Config)
        ConfigName = Config
        # sets Config name to be shown in UI
        try:
            App.UpdateShownConfig()
        except Exception:
            pass
        # used for closing window if there is one
        self.SetGameMaster = master
        if (
            self.SetGameMaster == None
            or self.SetGameMaster == False
            or self.SetGameMaster == ""
            or self.SetGameMaster == " "
        ):
            pass
        else:
            # does not need to close gloabal for this one
            # just the current window
            self.SetGameMaster.destroy()


class Bot:
    def __init__(self, Config, Running):
        self.Running = Running
        self.Config = Config

    def ManiaStart(self):
        if Config == "Osu":
            # loads Config file
            pass
        elif Config == "Quaver":
            # loads config file
            pass
        else:
            # loads custom config
            pass

        # will need to be updated to reflect the name of window found in Config
        try:
            Wincap = WindowCapture(None)
            Wincap.start()
            logger.info("Window Capture started")
        except Exception:
            logger.exception("Something went wrong while starting window capture\n")
            # sets button text if wincap fails to start
            Start_StopBTN.configure(text="START")
            self.Running = False

        while self.Running == True:
            # stops program from crashing when starting wincap
            if Wincap.screenshot is None:
                continue
            # used for stopping the bot and stopping the loop so the thread can be killed
            if Running == False:
                Wincap.stop()
                logger.info("Window Capture and Bot Stopped")
                break

            ScreenCap = Wincap.screenshot


# used for all UI elements including button functions!
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.functions = Functions()

        # sets for Config
        self.Fm = FileManager()

        self.master.geometry("500x650")
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

    # stop start command for the button :p
    def StartStop(self):
        """
        i am using threads because if i dont it will break tkinter's main loop
        and the UI and become unresponsive
        """
        global Running
        if Start_StopBTN["text"] == "START":
            Running = True
            # give current game and if it is running
            try:
                bot = Bot(Config, Running)
            except Exception:
                Running = False
                logger.exception("failed to give bot needed info")
                CloseGlobal(running=Running, master=self.master)

            try:
                self.t1 = threading.Thread(target=bot.ManiaStart)
                self.t1.start()
                logger.info("Started Thread for Bot")
                Start_StopBTN.configure(text="STOP")
            except Exception:
                logger.exception("Failed to start Thread for Bot\n")
                # sets button text if thread cant start
                Start_StopBTN.configure(text="START")
        elif Start_StopBTN["text"] == "STOP":
            try:
                # stops program
                Running = False
                self.t1.join()
                logger.info("Closed thread for Bot")
                Start_StopBTN.configure(text="START")
            except Exception:
                logger.exception("Failed to close the Bot thread\n")
                Start_StopBTN.configure(text="STOP")
        else:
            logger.warn("I dont even know man")

    # used for moving window when overidedirect(1) is active
    def SaveLastClickPos(self, event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    # used for moving window when overidedirect(1) is active
    def Dragging(self, event):
        x, y = (
            event.x - lastClickX + self.master.winfo_x(),
            event.y - lastClickY + self.master.winfo_y(),
        )
        self.master.geometry("+%s+%s" % (x, y))

    """
    Button Example:
        Button(self.master, text='TEXT', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg='#444444', fg='#fffafa',
                  padx=BUTTON_PADX, pady=BUTTON_PADY, relief=BUTTON_STYLE)
    Image Button Example:
        self.Image = ResizeImage(100, 100, r"UI-Media\icon-gear.png")
        self.Image = ImageTk.PhotoImage(self.Image)
        Button(image = self.Image, relief=BUTTON_STYLE, bg='#333333', fg='#fffafa').pack()
    """

    def ConfigSelect(self):
        if Running in [False, None]:
            global Config
            # loads config
            Config = self.Fm.LoadSettings()
            MultiConfig = Config["MultiConfig"]
            if MultiConfig in [True, "True", "true"]:
                # starts prompt to ask to load a config file
                Path = os.path.dirname(os.path.realpath(__file__))
                ConfigPath = Path.replace("\src", "")
                ConfigPath = "".join("Config")
                Config = filedialog.askopenfilename(
                    initialdir=ConfigPath,
                    title="Select Config",
                    filetypes=(("Config Files", "*.json"), ("all files", "*.*")),
                )
                print(Config)
            else:
                # runs change game if multi config is False
                self.functions.ChangeGame()
        else:
            messagebox.showwarning(
                "Bot is running",
                "The Bot is running please stop Bot before changing game or config",
            )

    def UpdateShownConfig(self):
        # destroys current lable
        self.ShownConfig.destroy()
        self.ShownConfig = None
        # remakes label
        self.ShownConfig = Label(
            self.master,
            font=BUTTON_FONT_BOLD,
            bg="#333333",
            fg="#fffafa",
            text="Current Loaded Config: " + ConfigName,
        )
        self.ShownConfig.pack()

    # Widgets
    def Create_Widgets(self):
        # Settings Button
        try:
            # loads icon
            try:
                self.SettingsIcon = ResizeImage(78, 78, r"UI-Media\icon-gear.png")
            except Exception:
                logger.exception(
                    "can not load or find needed icons for Settings Button\n"
                )

            self.SettingsIcon = ImageTk.PhotoImage(self.SettingsIcon)
            self.SettingsBTN = Button(
                self.master,
                image=self.SettingsIcon,
                relief="flat",
                bg="#333333",
                fg="#fffafa",
                padx=BUTTON_PADX,
                pady=BUTTON_PADY,
                borderwidth=0,
                activebackground="#363535",
                command=lambda: Settings(running=Running),
            )
            self.SettingsBTN.place(x=415, y=563)
        except Exception:
            CloseGlobal(master=None, running=Running)

        try:
            # loads icon
            try:
                self.ConfigIcon = ResizeImage(82, 82, r"UI-Media\Config-icon.png")
            except Exception:
                logger.exception("can not load or find needed icons\n")

            # used for changing games / configs
            self.ConfigIcon = ImageTk.PhotoImage(self.ConfigIcon)
            self.ConfigBTN = Button(
                self.master,
                image=self.ConfigIcon,
                relief="flat",
                bg="#333333",
                fg="#fffafa",
                padx=BUTTON_PADX,
                pady=BUTTON_PADY,
                borderwidth=0,
                activebackground="#363535",
                command=lambda: self.ConfigSelect(),
            )
            self.ConfigBTN.place(x=0, y=568)
        except Exception:
            CloseGlobal(master=None, running=Running)

        # Start / Stop Button
        try:
            global Start_StopBTN
            Start_StopBTN = Button(
                self.master,
                text="START",
                font=BUTTON_FONT_BOLD,
                width=BUTTON_WIDTH,
                height=BUTTON_HEIGHT,
                bg="#333333",
                fg="#fffafa",
                relief=BUTTON_STYLE,
                command=self.StartStop,
            )
            Start_StopBTN.place(x=190, y=255)
        except Exception:
            logger.exception(
                "something went very wrong while creating Start Stop Button\n"
            )
            CloseGlobal(master=None, running=Running)

        try:
            # shows Currently loaded config
            self.ShownConfig = Label(
                self.master,
                font=BUTTON_FONT_BOLD,
                bg="#333333",
                fg="#fffafa",
                text="Current Loaded Config: " + ConfigName,
            )
            self.ShownConfig.pack()
        except Exception:
            logger.exception("failed to create UI Lable for Loaded Config")
            CloseGlobal(master=None, running=Running)


class Run:
    def __init__(self):
        # global for if bot is running
        global Running
        # is set to None so UI can start
        Running = None
        # sets global for config name to be shown in UI
        global ConfigName
        ConfigName = ""

        CreateAppdataDir()

        # sets global for logger
        global logger
        loggerinit = Logger()
        loggerinit.CreateLogFolder()
        logger = loggerinit.StartLogger(name=__name__)

        # defines
        functions = Functions()
        Fm = FileManager()

        """
        Config Things
        """
        # checks if Config Files exist
        Fm.CreateConfigFolder()
        Fm.CreateConfigFiles()
        # loads settings for later use
        ConfigFile = Fm.LoadSettings()

        # used for checking if the json has all the needed keys
        # not done yet needs to be fixed!
        # UpdateConfig(Defualt_Config)

        # used for first run
        FirstRun().Run()

        # checks for running Games, needs to be run after config checking and first run check
        functions.Process()

        # Main Window Stuff
        try:
            root = tk.Tk()
            root.config(bg="#333333")
            root.resizable(width=False, height=False)
            root.attributes("-alpha", 0.965)
            ttk.Style().configure("TP.TFrame", background="snow")
            global App
            App = Application()
            # binds
            if ConfigFile["WindowDrag"] in [True, "True", "true"]:
                root.bind("<Button-1>", App.SaveLastClickPos)
                root.bind("<B1-Motion>", App.Dragging)

            root.protocol(
                "WM_DELETE_WINDOW", lambda: CloseGlobal(master=root, running=Running)
            )
            # root.overrideredirect(1)
            CenterWin(root)
            App.mainloop()
        except Exception as e:
            # shows error in logger
            logger.exception("something broke\n")


if __name__ == "__main__":
    Run()
