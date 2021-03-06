import sys
import tkinter as tk
from tkinter import colorchooser


class optionWindow:
    lines = open('settings.txt', 'r').readlines()  # reads the color from the file
    bgcolor = lines[0]  # initializes the color and is the point for all other windows to leach off it
    appFont = lines[1]  # initializes the font for the app to be changed later

    def menu(self):
        self.menuRoot = tk.Tk()
        self.menuRoot.resizable(False, False)
        self.menuRoot.geometry("300x300+1050+250")
        self.menuRoot.title("Options Menu")
        self.menuRoot.configure(bg=optionWindow.bgcolor)

        # button to change the bg color
        self.colorButton = tk.Button(self.menuRoot, text="Choose Color",
                                     command=lambda: optionWindow.choose_color(self))
        self.colorButton.place(x=170, y=8)

        # button to change the apps font/typeface
        self.fontButton = tk.Button(self.menuRoot, text="Change Font",
                                    command=lambda: optionWindow.changeTypeface(self))
        self.fontButton.place(x=170, y=48)

        # confirm button
        self.confirmButton = tk.Button(self.menuRoot, text="Confirm", command=lambda: optionWindow.updateMenu(self))
        self.confirmButton.place(relx=.5, rely=.9, anchor="center")

        self.labelOne = tk.Label(self.menuRoot, text="Change bg color: ", font=('Helvetica', 13),
                                 bg=optionWindow.bgcolor)
        self.labelOne.place(x=20, y=8)

        self.fontLabel = tk.Label(self.menuRoot, text="Change the font: ", font=('Helvetica', 13),
                                  bg=optionWindow.bgcolor)
        self.fontLabel.place(x=20, y=48)

    def choose_color(self):
        self.color_code = colorchooser.askcolor(title="Pick a Color")[1]  # opens a color wheel and saves the hex code

    def updateMenu(self):
        lines = open('settings.txt', 'r').readlines()
        lines[0] = self.color_code  # takes the saved color and initializes it
        # if statement to check if user changed color or not
        if lines[0]:
            out = open('settings.txt', 'w')
            out.writelines(lines)
            self.menuRoot.configure(bg=optionWindow.bgcolor)
            out.close()
            sys.exit()
        else:
            self.menuRoot.destroy()

    def changeTypeface(self):
        None
