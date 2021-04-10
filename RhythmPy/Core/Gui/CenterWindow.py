import tkinter


def CenterWin(win):
    """centers a tkinter window"""
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    win.deiconify()


# used for testing please ignore!
if __name__ == "__main__":
    root = tkinter.Tk()
    root.attributes("-alpha", 0.0)
    menubar = tkinter.Menu(root)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    frm = tkinter.Frame(root, bd=4, relief="raised")
    frm.pack(fill="x")
    lab = tkinter.Label(frm, text="Hello World!", bd=4, relief="sunken")
    lab.pack(ipadx=4, padx=4, ipady=4, pady=4, fill="both")
    CenterWin(root)
    root.attributes("-alpha", 1.0)
    root.mainloop()
