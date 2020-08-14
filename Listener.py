import tkinter as tk
import self
import fileinput

from OptionsMenu import optionWindow


class listener:

    def updatePass(self, name, num):
        self.bounds = num
        self.newRoot = tk.Tk()
        self.newRoot.resizable(False, False)
        self.newRoot.geometry("300x300+750+250")
        self.newRoot.title(name)
        self.newRoot.configure(bg=optionWindow.bgcolor)

        # dictionary to hold logo locations to display on top left of window
        serviceList = {
            "YouTube": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/ytlogo.ico',
            "Reddit": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/redditlogo.ico',
            "Amazon": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/amazonlogo.ico',
            "Twitter": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/twitterlogo.ico',
            "Spotify": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/spotifylogo.ico',
            "Google": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/googlelogo.ico',
            "GitHub": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/githublogo.ico',
            "Twitch": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/twitchlogo.ico',
            "Netflix": 'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/netflixlogo.ico'
        }

        self.newRoot.iconbitmap(serviceList[name])

        # base widgets to display
        self.passEntry = tk.Entry(self.newRoot, bd=3)
        self.passEntry.place(x=90, y=210)
        self.passLabel = tk.Label(self.newRoot, text="New Password: ")
        self.passLabel.place(x=110, y=185)
        self.passLabel.configure(bg=optionWindow.bgcolor)
        self.updateButton = tk.Button(self.newRoot, text="Update Password",
                                      command=lambda: listener.confirm(self, self.bounds),
                                      font=("Helvetica", 10, 'bold'),
                                      height=2, width=15)
        self.updateButton.place(x=90, y=250)
        self.lines = open('passwords.txt', 'r').readlines()
        self.currentPass = self.lines[self.bounds]
        self.textDisplay = tk.Label(self.newRoot, text=self.currentPass, font=("Helvetica", 25, 'bold'), bg=optionWindow.bgcolor)
        self.textDisplay.place(relx=.5, rely=.3, anchor="center")

    # changes the password to what is inside of the textfield
    def confirm(self, num):
        password = self.passEntry.get()  # holds new password from the Entry widget
        line = num  # the line to be written to (changes depending on button chosen)
        listener.replace_line(self, 'passwords.txt', line, password)

    def replace_line(self, fileName, lineNum, text):
        lines = open(fileName, 'r').readlines()
        lines[lineNum] = text + '\n'  # adds '\n' so it keeps all other lines in tact, otherwise is slides what is
        # below of it, to the line being edited
        out = open(fileName, 'w')
        out.writelines(lines)
        self.textDisplay.configure(text=lines[lineNum])  # updates password on screen before closing txt file
        out.close()
