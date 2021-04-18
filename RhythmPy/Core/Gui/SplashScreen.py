import tkinter as tk
from Core.Gui import CenterWin
import time
from PIL import Image, ImageTk


class SplashScreen:
    def Start(self):
        self.master = tk.Tk()
        canvas = tk.Canvas(self.master)
        canvas.pack(expand=True)
        op = Image.open(r"Assets/UI/Splash.png")
        SplashImage = ImageTk.PhotoImage(op)
        Splash = tk.Label(self.master, image=SplashImage)
        Splash.image = SplashImage
        Splash.place(x=-2, y=-2)
        self.master.geometry("620x300")
        self.master.overrideredirect(True)
        self.master.attributes("-topmost", True)
        CenterWin(self.master)
        self.master.update()

    def Stop(self):
        print("killed splash screen")
        self.master.destroy()


if __name__ == "__main__":
    splash = SplashScreen()
    splash.Start()
    time.sleep(1)
    splash.Stop()
