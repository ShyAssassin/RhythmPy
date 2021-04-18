try:
    import tkinter as tk
    from tkinter import Button, Label, filedialog, messagebox, ttk
except (ImportError, ModuleNotFoundError):
    import Tkinter as tk
    from Tkinter import ttk, Button, Label, messagebox, filedialog

import os

from PIL import ImageTk

from Core import (
    Gui,
    CloseGlobal,
    FileManager,
    Logger,
    Paths,
)
from Core.Bot import Bot

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


# used for all UI elements including button functions!
class Application(tk.Frame):
    def __init__(self, master=None):
        self.Running = False
        super().__init__(master)
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

    def StartStop(self):
        if self.Start_StopBTN["text"] == "START" and "Config" in dir(self):
            try:
                self.Running = True
                Bot.Start(Running=self.Running, Config=self.Config)
                self.Start_StopBTN.configure(text="STOP")
            except Exception:
                self.tart_StopBTN.configure(text="START")
                logger.exception("Failed to Start bot\n")
        elif self.Start_StopBTN["text"] == "STOP":
            try:
                Bot.Stop()
                self.Running = False
                self.Start_StopBTN.configure(text="START")
            except Exception:
                self.Start_StopBTN.configure(text="STOP")
                logger.exception("Failed to stop bot\n")
        else:
            messagebox.showwarning(
                "No Config", "No Config is currently loaded, load one to continue."
            )

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

    def ConfigSelect(self):
        if self.Running in [False, None]:
            # starts prompt to ask to load a config file
            ConfigPath = Paths.AppDataConfigDir()
            self.Config = filedialog.askopenfilename(
                initialdir=ConfigPath,
                title="Select Config",
                filetypes=(("Config Files", "*.json"), ("all files", "*.*")),
            )
            # gets files base name and removes .json
            if self.Config != "":
                self.ConfigName = str(
                    os.path.basename(self.Config).replace(".json", "")
                )
                self.UpdateShownConfig()
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
            text="Current Loaded Config: " + self.ConfigName,
        )
        self.ShownConfig.pack()

    # Widgets
    def Create_Widgets(self):
        # Settings Button
        try:
            # loads icon
            try:
                self.SettingsIcon = Gui.ResizeImage(78, 78, r"Assets/UI/icon-gear.png")
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
                command=lambda: Gui.Settings(running=self.Running),
            )
            self.SettingsBTN.place(x=415, y=563)
        except Exception:
            CloseGlobal(master=None, running=False)

        try:
            # loads icon
            try:
                self.ConfigIcon = Gui.ResizeImage(82, 82, r"Assets/UI/Config-icon.png")
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
            CloseGlobal(master=None, running=False)

        # Start / Stop Button
        try:
            self.Start_StopBTN = Button(
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
            self.Start_StopBTN.place(x=190, y=255)
        except Exception:
            logger.exception(
                "something went very wrong while creating Start Stop Button\n"
            )
            CloseGlobal(master=None, running=False)

        try:
            # shows Currently loaded config
            self.ConfigName = "None"
            self.ShownConfig = Label(
                self.master,
                font=BUTTON_FONT_BOLD,
                bg="#333333",
                fg="#fffafa",
                text="Current Loaded Config: " + self.ConfigName,
            )
            self.ShownConfig.pack()
        except Exception:
            logger.exception("failed to create UI Lable for Loaded Config")
            CloseGlobal(master=None, running=False)


class Run:
    def __init__(self):
        # sets global for logger
        global logger
        loggerinit = Logger()
        loggerinit.CreateLogFolder()
        logger = loggerinit.StartLogger(name=__name__)

        # loads settings for later use
        SettingsFile = FileManager.LoadSettings()

        # Main Window Stuff
        try:
            root = tk.Tk()
            root.config(bg="#333333")
            root.resizable(width=False, height=False)
            root.wait_visibility()
            root.attributes("-alpha", 0.965)
            ttk.Style().configure("TP.TFrame", background="snow")
            App = Application()
            # binds
            if SettingsFile["WindowDrag"] in [True, "True", "true"]:
                root.bind("<Button-1>", App.SaveLastClickPos)
                root.bind("<B1-Motion>", App.Dragging)

            root.protocol(
                "WM_DELETE_WINDOW",
                lambda: CloseGlobal(master=root, running=App.Running),
            )
            # root.overrideredirect(1)
            Gui.CenterWin(root)
            App.mainloop()
        except Exception:
            # shows error in logger
            logger.exception("something broke\n")


if __name__ == "__main__":
    Run()
