import tkinter as tk
from Core.Gui import CenterWin
import PIL


class SplashScreen:
    def Start(self):
        self.master = tk.Tk()
        canvas = tk.Canvas(self.master)
        canvas.pack(expand=True)
        # load splash screen asset
        ImageAsset = PIL.Image.open(r"Assets/UI/Splash.png")
        Image = PIL.ImageTk.PhotoImage(ImageAsset)
        SplashScreen = tk.Label(self.master, image=Image)
        SplashScreen.image = Image
        SplashScreen.place(x=-2, y=-2)
        self.master.geometry("620x300")
        self.master.overrideredirect(True)
        # force window the be ontop of everything else
        self.master.attributes("-topmost", True)
        CenterWin(self.master)
        # we cant start the window mainloop because that will then take over the main thread and block other code from running
        # so we update it once and the app will "hang" until we have initialized the main tkinter window and other systems
        self.master.update()

    def Stop(self):
        print("killed splash screen")
        self.master.destroy()
