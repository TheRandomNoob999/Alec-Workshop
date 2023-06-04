import random
import math
import GameData
import subprocess
from tkinter import *
from tkinter import ttk

def openShop():
    saveGame()
    subprocess.Popen(["python", "Shop.pyw"], shell = True)

class game():
    def __init__(self, day, health, money, sleep, hunger, job, bed):
        self.day = day
        self.health = health
        self.money = money
        self.sleep = sleep
        self.hunger = hunger
        self.job = job
        self.bed = int(bed)

    def rewrite(self):
        if(self.health > 100):
            self.health = 100
        if(self.hunger > 100):
            self.hunger = 100
        if(self.sleep > 100):
            self.sleep = 100
        math.ceil(self.money)
        _Day.set("Day " + str(self.day))
        _healthStat.set("Health = " + str(self.health) + "%")  
        _moneyStat.set("Money = $" + str(self.money))
        _sleepStat.set("Sleep = " + str(self.sleep) + "%")
        _HungerStat.set("Hunger = " + str(self.hunger) + "%")
        _Summary.set("Summary: " + _Explanation.get())
    
    def nextDay(self, action):
        self.day += 1
        _EventCountdown.set(_EventCountdown.get() - 1)
        _Event.set("Next event happening in " + str(_EventCountdown.get()) + " Days")

        if (_EventCountdown.get() == 0):
            self.randomEvent()
            _EventCountdown.set(_EventMax.get())

        if(action == "Work"):
            _Explanation.set("All in a hard days work")
        elif(action == "Sleep"):
            _Explanation.set("Lets just sleep")
        elif(action == "Eat"):
            _Explanation.set("I ate all day")

        if(_JobClose.get() > 0):
            _JobClose.set(_JobClose.get() - 1)
            if(_JobClose.get() == 0):
                workButton["state"] = "enabled"
        
        if(self.hunger <= 0):
            self.health -= 10
        self.rewrite()
        if(self.health <= 0):
            _Explanation.set("You died lol")
        
    def randomEvent(self):
        #Each Event
        events = ["Tax Day", "Sickness", "Doctor", "Fundraiser"]
        eventChoice = events[random.randint(0, len(events) - 1)]
        if (eventChoice == "Tax Day"):
            self.money = self.money * 0.8
            _EventSummary.set("Time to give 1/3 of your money to the Government")
        elif (eventChoice == "Sickness"):
            sickRandom = random.randint(1, 3)
            if (sickRandom == 1):
                self.sleep -= 100
                _EventSummary.set("Looks like you caught the flu,\n take some time to rest up")
                self.health -= 25
            elif (sickRandom == 2):
                self.sleep = -25
                self.hunger -= 100
                _EventSummary.set("Looks like you ate something bad")
            elif (sickRandom == 3):
                _EventSummary.set("A sickness has gone through your job place leaving it closed \n I guess there's no work for a lil while")
                workButton["state"] = "disabled"
                _JobClose.set(random.randint(2, 5))
            
        elif (eventChoice == "Doctor"):
            self.money -= 100
            self.health = 100
            _EventSummary.set("You had a sore throat so you went to the doctors. \nYou're perfectly fine! (-$100)")
        elif (eventChoice == "Fundraiser"):
            self.money - 50
            _EventSummary.set("Some Girlscouts came to your door.\n You just had to buy some thin mints")
        
        _Event.set("The event is " + eventChoice + ", Horray!")
        self.rewrite()

    def work(self):
        #Job Paychecks
        jobPayments = [30]
        jobEnergy = [20]
        if (self.sleep >= jobEnergy[self.job] + (_JobStreak.get() * 4) and self.health > 0 and _JobClose.get() == 0):
            self.nextDay("Work")
            self.money += jobPayments[self.job]
            self.sleep = (self.sleep - (jobEnergy[self.job] + (_JobStreak.get() * 4))) 
            _JobStreak.set(_JobStreak.get() + 1)
            self.hunger -= 10
        self.rewrite()

    def goSleep(self):
        bedEnergy = [20, 30, 50, 100]
        if(self.sleep < 100):
            self.sleep += bedEnergy[self.bed]
            self.hunger -= 15
            self.health += 15
            _JobStreak.set(0)
        self.rewrite()

    def eat(self):
        if (self.health > 0):
            for index, X in enumerate(foodMenu, start=0):
                if(X == _foodOption.get()):
                    if(self.money >= foodCost[index]):
                        self.money -=foodCost[index]
                        if(foodChange[index] == "F"):
                            self.hunger += foodValue[index]
                        if(foodChange[index] == "E"):
                            self.sleep += foodValue[index]
                        if(foodChange[index] == "H"):
                            self.health += foodValue[index]
                        self.nextDay("Eat")
        self.rewrite()

if (GameData.loadData()[0] > 1):
    player = game(GameData.loadData()[0], GameData.loadData()[1], GameData.loadData()[2], GameData.loadData()[3], GameData.loadData()[4], GameData.loadData()[5], GameData.loadData()[6])
else:
    player = game(1, 100, 200, 100, 100, 0, 0)

root = Tk()
root.title("Life")

def saveGame():
    GameData.saveData(player.day, player.health, player.money, player.sleep, player.hunger, player.job, player.bed)

#Hidden Variables
_JobStreak = IntVar()
_JobStreak.set(0)
_JobClose = IntVar()
_JobClose.set(0)

#The Main Window Application
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#The stats labels
_Day = StringVar()
_Day.set("Day " + str(player.day))
dayLabel = ttk.Label(mainframe, textvariable=_Day)
dayLabel.grid(column=1, row=1, sticky=(NSEW))

_Stats = StringVar()
_Stats.set("Status")
statsLabel = ttk.Label(mainframe, textvariable=_Stats)
statsLabel.grid(column=1, row=2, sticky=(NSEW))

_healthStat = StringVar()
_healthStat.set("Health = " + str(player.health) + "%") 
healthLabel = ttk.Label(mainframe, textvariable=_healthStat)
healthLabel.grid(column=1, row=3, sticky=(NSEW))

_moneyStat = StringVar()
_moneyStat.set("Money = $" + str(player.money))
moneyLabel = ttk.Label(mainframe, textvariable=_moneyStat)
moneyLabel.grid(column=1, row=4, sticky=(NSEW))

_sleepStat = StringVar()
_sleepStat.set("Sleep = " + str(player.sleep) + "%") 
sleepLabel = ttk.Label(mainframe, textvariable=_sleepStat)
sleepLabel.grid(column=1, row=5, sticky=(NSEW))

_HungerStat = StringVar()
_HungerStat.set("Hunger = " + str(player.hunger) + "%")
hungerLabel = ttk.Label(mainframe, textvariable=_HungerStat)
hungerLabel.grid(column=1, row=6)

#The action Buttons
actionsLabel = ttk.Label(mainframe, text="Actions").grid(column=2, row=2, sticky=(NSEW))

workButton = ttk.Button(mainframe, text="Work", command= lambda: player.work()).grid(column=2, row=4)

sleepButton = ttk.Button(mainframe, text="Sleep", command= lambda: player.goSleep()).grid(column=2, row=5)

eatButton = ttk.Button(mainframe, text="Eat", command= player.eat).grid(column=2, row=6)

shopButton = ttk.Button(mainframe, text="Shop", command= openShop)

#Summary + Events
_Explanation = StringVar()
_Explanation.set("New Life, New Me")
_Summary = StringVar()
_Summary.set("Summary: " + _Explanation.get())
summaryLabel = ttk.Label(mainframe, textvariable=_Summary)
summaryLabel.grid(column=0, row=1)

_EventMax = IntVar()
_EventMax.set(10)
_EventCountdown = IntVar()
_EventCountdown.set(_EventMax.get())
_Event = StringVar()
_Event.set("Next event happening in " + str(_EventCountdown.get()) + " Days")
eventLabel = ttk.Label(mainframe, textvariable=_Event)
eventLabel.grid(column=0, row=2)

_EventSummary = StringVar()
eventSummaryLabel = ttk.Label(mainframe, textvariable=_EventSummary)
eventSummaryLabel.grid(column=0, row=3)

#Dropdown Menus
foodCost = [12, 10, 25, 10, 40]
foodChange = ["F", "F", "E", "H", "F"]
foodValue = [30, 10, 75, 35, 50]
foodName = ["Burger", "Fries", "Energy Drink", "Small Pills", "Might Steak"]
foodMenu = [
    "$"+str(foodCost[0])+" "+foodName[0]+" "+foodChange[0]+str(foodValue[0]),
    "$"+str(foodCost[1])+" "+foodName[1]+" "+foodChange[1]+str(foodValue[1]),
    "$"+str(foodCost[2])+" "+foodName[2]+" "+foodChange[2]+str(foodValue[2]),
    "$"+str(foodCost[3])+" "+foodName[3]+" "+foodChange[3]+str(foodValue[3]),
    "$"+str(foodCost[4])+" "+foodName[4]+" "+foodChange[4]+str(foodValue[4])
    ]

#Change Actions
_foodOption = StringVar()
_foodOption.set(foodMenu[0])
foodDrop = ttk.OptionMenu(mainframe, _foodOption, *foodMenu)
foodDrop.grid(column=3, row=6)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

saveButton = ttk.Button(mainframe, text="Save Game", command=saveGame).grid(column=3, row=1, sticky=(NSEW))

root.mainloop()