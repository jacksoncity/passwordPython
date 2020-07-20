from tkinter import *
from Listener import *


class Window:
    def __init__(self):
        root = Tk()
        root.geometry("450x450")
        root.title("Password Keeper")

        # YouTube
        youTube = Button(root, text="YouTube", command=updatePass("YouTube", 0), font=("Helvetica", 15),
                         height=1, width=8)
        youTube.place(x=40, y=40)

        # Reddit
        reddit = Button(root, text="Reddit", command=updatePass("Reddit", 1), font=("Helvetica", 15), height=1, width=8)
        reddit.place(x=175, y=40)

        root.mainloop()


Window()
