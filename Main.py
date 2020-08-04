import tkinter as tk
import Listener
from Listener import *
from OptionsMenu import *


root = tk.Tk()
root.resizable(False, False)
root.geometry("450x450+680+130")
root.title("Password Keeper")
root.configure(bg="gray")
root.iconbitmap(
    'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/keyicon.ico')

# paths for buttons placed on the main window
youTube = tk.Button(root, text="YouTube", command=lambda: listener.updatePass(self, "YouTube", 0), font=("Helvetica", 15),
                    height=1, width=8)
youTube.place(x=40, y=40)

reddit = tk.Button(root, text="Reddit", command=lambda: listener.updatePass(self, "Reddit", 1), font=("Helvetica", 15),
                   height=1, width=8)
reddit.place(x=180, y=40)

amazon = tk.Button(root, text="Amazon", command=lambda: listener.updatePass(self, "Amazon", 2), font=("Helvetica", 15),
                   height=1, width=8)
amazon.place(x=320, y=40)

twitter = tk.Button(root, text="Twitter", command=lambda: listener.updatePass(self, "Twitter", 3), font=("Helvetica", 15),
                   height=1, width=8)
twitter.place(x=40, y=110)

spotify = tk.Button(root, text="Spotify", command=lambda: listener.updatePass(self, "Spotify", 4), font=("Helvetica", 15),
                   height=1, width=8)
spotify.place(x=180, y=110)

google = tk.Button(root, text="Google", command=lambda: listener.updatePass(self, "Google", 5), font=("Helvetica", 15),
                   height=1, width=8)
google.place(x=320, y=110)

gitHub = tk.Button(root, text="GitHub", command=lambda: listener.updatePass(self, "GitHub", 6), font=("Helvetica", 15),
                   height=1, width=8)
gitHub.place(x=40, y=180)

twitch = tk.Button(root, text="Twitch", command=lambda: listener.updatePass(self, "Twitch", 7), font=("Helvetica", 15),
                   height=1, width=8)
twitch.place(x=180, y=180)

netflix = tk.Button(root, text="Netflix", command=lambda: listener.updatePass(self, "Netflix", 8), font=("Helvetica", 15),
                   height=1, width=8)
netflix.place(x=320, y=180)

# options button
options = tk.Button(root, text="Options", command=lambda: optionWindow.menu(self), font=("Helvetica", 8),
                   height=1, width=6)
options.place(x=5, y=5)

root.mainloop()
