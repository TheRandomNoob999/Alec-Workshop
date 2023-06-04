from tkinter import *
from tkinter import ttk
import GameData

bedPrices = [200, 500, 1000]

def buy(item, number):
    money = GameData.loadData()[2]
    print("buy")

    if(item == "Bed"):
        print("bed")
        currentBed = GameData.loadData()[6]
        if(money >= bedPrices[number] and number + 1 > currentBed):
            money -= bedPrices[number]
            GameData.saveData(GameData.loadData()[0], GameData.loadData()[1], money, GameData.loadData()[3], GameData.loadData()[4], GameData.loadData()[5], number + 1)
            print("Bought Bed")

root = Tk()
root.title("Shop")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Welcome to the Shop", font=("David",15)).grid(column=0, row=0, sticky=(NSEW))
ttk.Label(mainframe, text="The Game will automatically save\nif you buy something", font=("David",10)).grid(column=0, row=1, sticky=(NSEW))
ttk.Label(mainframe, text="These upgrades are specific to this save", font=("David",10)).grid(column=0, row=2, sticky=(NSEW))

_SMLabel = ttk.Label(mainframe, text="Spring Mattress +30E").grid(column=1, row=1, sticky=(NSEW))
_SMPrice = StringVar(); _SMPrice.set("200")
_SMButton = ttk.Button(mainframe, textvariable=_SMPrice, command=lambda:buy("Bed", 0)).grid(column=2, row=1, sticky=(NSEW))

_GMLabel = ttk.Label(mainframe, text="Gell Mattress +50E").grid(column=1,row=2, sticky=(NSEW))
_GMPrice = StringVar(); _GMPrice.set("500")
_GMButton = ttk.Button(mainframe, textvariable=_GMPrice).grid(column=2, row=2)

_KMLabel = ttk.Label(mainframe, text="King Bed +100E").grid(column=1,row=3, sticky=(NSEW))
_KMPrice = StringVar(); _KMPrice.set("1000")
_KMButton = ttk.Button(mainframe, textvariable=_KMPrice).grid(column=2, row=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
root.mainloop()