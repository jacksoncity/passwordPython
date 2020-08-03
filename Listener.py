import tkinter as tk
import self


# FIND A WAY TO POLYMORPH THESE LISTENERS (assign a str value and int value??)


class listener:

    def updatePass(self, name, num):
        self.bounds = num
        self.newRoot = tk.Tk()
        self.newRoot.geometry("300x300")
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

    # changes the password to what is inside of te textfield
    def confirm(self, num):
        password = self.passEntry.get()
        print(password)
