def CenterWin(window):
    """Centers a tkinter window"""
    window.update_idletasks()
    Width = window.winfo_width()
    FrameWidth = window.winfo_rootx() - window.winfo_x()
    WindowWidth = Width + 2 * FrameWidth
    Height = window.winfo_height()
    TitleBarHeight = window.winfo_rooty() - window.winfo_y()
    WindowHeight = Height + TitleBarHeight + FrameWidth
    # calculate the position the window should be placed
    x = window.winfo_screenwidth() // 2 - WindowWidth // 2
    y = window.winfo_screenheight() // 2 - WindowHeight // 2
    window.geometry("{}x{}+{}+{}".format(Width, Height, x, y))
    window.deiconify()
