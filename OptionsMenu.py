import tkinter as tk


class optionWindow:

    def menu(self):
        self.menuRoot = tk.Tk()
        self.menuRoot.resizable(False, False)
        self.menuRoot.geometry("300x300+750+250")
        self.menuRoot.title("Options Menu")
        self.menuRoot.configure(bg="grey")

        # Drop down menu of colors to choose from
        colorMenu = [
            "White", "Gray", "Black", "Red", "Blue", "Green", "Pink", "Purple", "Yellow"
        ]
        variable = tk.StringVar(self.menuRoot)
        variable.set(colorMenu[0])

        self.opt = tk.OptionMenu(self.menuRoot, variable, *colorMenu)
        self.opt.config(font=('Helvetica', 13))
        self.opt.place(x=180, y=3)

        self.labelOne = tk.Label(self.menuRoot, text="Change bg color: ", font=('Helvetica', 13), bg="Gray")
        self.labelOne.place(x=3, y=8)
