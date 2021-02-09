# this isnt in modules because it is related to ui and not "back end"
import tkinter as tk
from Modules import CenterWin


class SplashScreen:
    def __init__(self):
        self.master = tk.Tk()
        canvas = tk.Canvas(self.master)
        self.master.geometry("620x300")
        self.master.overrideredirect(True)
        CenterWin(self.master)

    def Start(self):
        self.master.mainloop()

    def Stop(self):
        self.master.destroy()
        print("killed splash screen")


if __name__ == "__main__":
    SplashScreen().Start()
