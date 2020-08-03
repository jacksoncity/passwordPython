import tkinter as tk
import self
import fileinput


# FIND A WAY TO POLYMORPH THESE LISTENERS (assign a str value and int value??)


class listener:

    def updatePass(self, name, num):
        self.bounds = num
        self.newRoot = tk.Tk()
        self.newRoot.resizable(False, False)
        self.newRoot.geometry("300x300+750+250")
        self.newRoot.title(name)

        # check name to correspond to logo in top right
        if name == "YouTube":
            self.newRoot.iconbitmap(
                'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/ytlogo.ico')
        elif name == "Reddit":
            self.newRoot.iconbitmap(
                'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/redditlogo.ico')
        elif name == "Amazon":
            self.newRoot.iconbitmap(
                'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/amazonlogo.ico')
        else:
            self.newRoot.iconbitmap(
                'c:/Users/jacks/Documents/DESKTOP/Personal_Programming/passwordPython/icons/keyicon.ico')

        # base widgets to display
        self.passEntry = tk.Entry(self.newRoot, bd=3)
        self.passEntry.place(x=90, y=210)
        self.passLabel = tk.Label(self.newRoot, text="New Password: ")
        self.passLabel.place(x=110, y=185)
        self.updateButton = tk.Button(self.newRoot, text="Update Password",
                                      command=lambda: listener.confirm(self, self.bounds),
                                      font=("Helvetica", 10, 'bold'),
                                      height=2, width=15)
        self.updateButton.place(x=90, y=250)
        self.lines = open('passwords.txt', 'r').readlines()
        self.currentPass = self.lines[self.bounds]
        self.textDisplay = tk.Label(self.newRoot, text = self.currentPass, font=("Helvetica", 25, 'bold'))
        self.textDisplay.place(relx=.5, rely=.3, anchor="center")

    # changes the password to what is inside of te textfield
    def confirm(self, num):
        password = self.passEntry.get()  # holds new password from the Entry widget
        line = num  # hte line to be written to (changes depending on button chosen)
        listener.replace_line(self, 'passwords.txt', line, password)

    def replace_line(self, fileName, lineNum, text):
        lines = open(fileName, 'r').readlines()
        lines[lineNum] = text + '\n'  # adds '\n' so it keeps all other lines in tact, otherwise is slides whats
                                      # in front of it to the line being edited
        out = open(fileName, 'w')
        out.writelines(lines)
        out.close()
