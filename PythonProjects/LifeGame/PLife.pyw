from tkinter import *
from tkinter import ttk
import subprocess
import sys
import os
from GameData import deleteData

dataFile = os.path.abspath("Game.pyw")

def play():
    subprocess.Popen(["python", dataFile], shell = True)
    sys.exit(0)

def reset():
    deleteData()

root = Tk()
root.title("Life")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

dayLabel = ttk.Label(mainframe, text="Welcome to PLife", font=("David", 25))
dayLabel.grid(column=1, row=1, sticky=(NSEW))

nameLabel = ttk.Label(mainframe, text="By Alec", font=("David",15))
nameLabel.grid(column=1, row= 2, sticky=(NSEW))

playButton = ttk.Button(mainframe, text="Play", command=play)
playButton.grid(column=1, row=3, sticky=(NSEW))

clearButton = ttk.Button(mainframe, text="Clear Data", command=reset).grid(column=1, row=4, sticky=(NSEW))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()