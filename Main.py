import tkinter as tk

import Listener
from Listener import *

root = tk.Tk()
root.geometry("450x450")
root.title("Password Keeper")
root.iconbitmap(
    'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/keyicon.ico')

# YouTube
youTube = tk.Button(root, text="YouTube", command=lambda: listener.updatePass(self, "YouTube", 0), font=("Helvetica", 15),
                    height=1, width=8)
youTube.place(x=40, y=40)

reddit = tk.Button(root, text="Reddit", command=lambda: listener.updatePass(self, "Reddit", 0), font=("Helvetica", 15),
                   height=1, width=8)
reddit.place(x=180, y=40)

amazon = tk.Button(root, text="Amazon", command=lambda: listener.updatePass(self, "Amazon", 0), font=("Helvetica", 15),
                   height=1, width=8)
amazon.place(x=320, y=40)


root.mainloop()
