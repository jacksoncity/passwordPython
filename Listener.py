from tkinter import *


# FIND A WAY TO POLYMORPH THESE LISTENERS (assign a str value and int value??)

def updatePass(name, num):
    newRoot = Tk()
    newRoot.geometry("300x300")
    newRoot.title(name)
    updateButton = Button(newRoot, text="Update Password", command=read(num), font=("Helvetica", 10, 'bold'),
                          height=2, width=15)
    updateButton.place(x=90, y=250)


def read(num):
    readFile = open("passwords.txt", 'r')
    print(readFile.readline())

    readFile.close()
