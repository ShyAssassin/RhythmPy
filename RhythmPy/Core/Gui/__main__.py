import tkinter as tk
from tkinter import Button, Label, filedialog, messagebox, ttk
from PIL import ImageTk
from Core import Gui, CloseGlobal, FileManager, Logger, Paths, Settings
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
class RhythmPy(tk.Frame):
    """The GUI for RhythmPy"""

    def __init__(self, master=None):
        self.Running = False
        super().__init__(master)
        self.master.geometry("500x650")
        self.master.title("RhythmPy")
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
        # checks if Config as been initialized and if bot is running
        if self.Start_StopBTN["text"] == "START" and "Config" in dir(self):
            try:
                self.Running = True
                self.bot = Bot(Running=self.Running, ConfigFile=self.Config)
                self.bot.Start()
                self.Start_StopBTN.configure(text="STOP")
            except Exception:
                self.Start_StopBTN.configure(text="START")
                logger.exception("Failed to Start bot\n")
        elif self.Start_StopBTN["text"] == "STOP":
            try:
                self.bot.Stop()
                self.Running = False
                self.Start_StopBTN.configure(text="START")
            except Exception as e:
                self.Start_StopBTN.configure(text="STOP")
                messagebox.showerror(
                    "Failed to Start",
                    "The bot failed to start\n %s",
                    e.with_traceback(),
                )
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
        """Creates File dialog for getting Config Files"""
        if self.Running in [False, None]:
            # starts prompt to ask to load a config file
            ConfigPath = Paths.AppDataConfigDir()
            self.Config = filedialog.askopenfilename(
                initialdir=ConfigPath,
                title="Select Config",
                filetypes=(("Config Files", "*.json"), ("all files", "*.*")),
            )
            # gets Config name and sets ConfigName
            if self.Config != "":
                try:
                    self.ConfigName = FileManager.LoadConfig(self.Config)
                    self.ConfigName = self.ConfigName["Name"]
                    self.UpdateShownConfig()
                except KeyError:
                    logger.exception("Invalid Config loaded\n")
                    LogFile = str(self.appdatapath + self.CurrentDate + ".log")
                    messagebox.showerror(
                        "Config Error",
                        "Invalid Config\nCheck Logs for details. %s" % LogFile,
                    )
        else:
            messagebox.showwarning(
                "Bot is running",
                "The Bot is running please stop Bot before changing game or config",
            )

    def UpdateShownConfig(self):
        """Updates Currently showed Config"""
        # destroys current lable
        self.ShownConfig.destroy()
        self.ShownConfig = None
        # remake label with updated info
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
        """Create all UI elements"""
        # Load all needed UI assets
        try:
            self.SettingsIcon = Gui.ResizeImage(76, 76, r"Assets/UI/icon-gear.png")
            self.ConfigIcon = Gui.ResizeImage(82, 82, r"Assets/UI/Config-icon.png")
        except Exception:
            logger.exception("Failed to load UI assets\n")

        # create all on screen buttons
        try:
            # Creates settings Button
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
                command=lambda: Settings.Run(),
            )
            self.SettingsBTN.place(x=415, y=565)

            # Create config button
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

            # Create Start / Stop button
            self.Start_StopBTN = Button(
                self.master,
                text="START",
                font=BUTTON_FONT_BOLD,
                width=BUTTON_WIDTH,
                height=BUTTON_HEIGHT,
                bg="#333333",
                fg="#fffafa",
                bd=0,
                relief=BUTTON_STYLE,
                borderwidth=1,
                pady=0,
                padx=0,
                command=self.StartStop,
            )
            self.Start_StopBTN.place(x=185, y=255)

            # Create label for currently loaded config
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
            logger.exception("Failed to create UI elements\n")
            CloseGlobal(master=None, running=False)


def Run():
    # sets global for logger
    global logger
    logger = Logger()
    logger.CreateLogFolder()
    logger = logger.StartLogger(name=__name__)

    # loads settings for later use
    SettingsFile = FileManager.LoadSettings()

    # Main Window Stuff
    try:
        root = tk.Tk()
        root.config(bg="#333333")
        root.resizable(width=False, height=False)
        root.wait_visibility()
        root.attributes("-alpha", 0.965)
        Style = ttk.Style(root)
        Style.configure("TP.TFrame", background="snow")
        App = RhythmPy()
        # binds
        if SettingsFile["WindowDrag"] in [True, "True", "true"]:
            root.bind("<Button-1>", App.SaveLastClickPos)
            root.bind("<B1-Motion>", App.Dragging)

        root.protocol(
            "WM_DELETE_WINDOW",
            lambda: CloseGlobal(master=root, running=App.Running),
        )
        Gui.CenterWin(root)
        App.mainloop()
    except Exception:
        logger.exception("Failed to start RhythmPy GUI\n")


if __name__ == "__main__":
    Run()
