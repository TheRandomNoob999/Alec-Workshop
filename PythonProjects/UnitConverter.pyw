from tkinter import *
from tkinter import ttk

units = {
    "Feet" : {
        "Meters" : 0.3048,
        "Yards" : 0.333333,
        "Centimeters" : 30.48,
        "Miles" : 0.000189394,
        "Kilometers" : 0.0003048,
        "Inches" : 12,
        "Feet" : 1
    },
    "Meters" : {
        "Feet" : 3.28084,
        "Yards" : 1.09361,
        "Centimeters" : 100,
        "Miles" : 0.000621371,
        "Kilometers" : 0.001,
        "Inches" : 39.3701,
        "Meters" : 1
    },
    "Yards" : {
        "Feet" : 3,
        "Meters" : 0.9144,
        "Centimeters" : 91.44,
        "Miles" : 0.000568182,
        "Kilometers" : 0.0009144,
        "Inches" : 36,
        "Yards" : 1
    },
    "Centimeters" : {
        "Feet" : 0.0328084,
        "Meters" : 0.01,
        "Yards" : 0.0109361,
        "Miles" : 6.2137e-6,
        "Kilometers" : 1e-5,
        "Inches" : 0.393701,
        "Centimeters" : 1
    },
    "Miles" : {
        "Feet" : 5280,
        "Meters" : 1609.34,
        "Yards" : 1760,
        "Centimeters" : 160934,
        "Kilometers" : 1.60934,
        "Inches" : 63360,
        "Miles" : 1
    },
    "Kilometers" : {
        "Feet" : 3280.84,
        "Meters" : 1000,
        "Yards" : 1093.61,
        "Centimeters" : 100000,
        "Miles" : 0.621371,
        "Inches" : 39370.1,
        "Kilometers" : 1
    },
    "Inches" : {
        "Feet" : 0.0833333,
        "Meters" : 0.0254,
        "Yards" : 0.0277778,
        "Centimeters" : 2.54,
        "Miles" : 1.5783e-5,
        "Kilometers" : 2.54e-5,
        "Inches" : 1
    },
}

options = [
    "Feet",
    "Meters",
    "Yards",
    "Centimeters",
    "Miles",
    "Kilometers",
    "Inches",
    "Feet"
]

def calculate(*args):
    try:
            converstionIn = units[_convertInput.get()].get(convertOutput)
            balancer = 10000.0
            _output.set(int(float(_input_entry.get()) * converstionIn * balancer + 0.5)/balancer)
    except:
        pass

def reverse(*args):
    global convertInput
    global convertOutput
    global _convertInput
    global _convertOutput
    convertInput = _convertInput.get()

    oldConvertInput = convertInput
    oldConvertOutput = convertOutput
    convertInput = oldConvertOutput
    convertOutput = oldConvertInput
    _convertInput.set(convertInput)
    _convertOutput.set(convertOutput)
    calculate()

root = Tk()
_convertInput = StringVar(master=root, value="Feet")
_convertOutput = StringVar(master=root, value="Meters")

convertInput = "Feet"
convertOutput = "Meters"
root.title("Unit Conversions")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

_input = StringVar()
_input_entry = ttk.Entry(mainframe, width=7, textvariable=convertInput)
_input_entry.grid(column=2, row=1, sticky=(W, E))

_output = StringVar()
ttk.Label(mainframe, textvariable=_output).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

inputText = ttk.OptionMenu(mainframe, _convertInput, *options)
inputText.grid(column=3, row=1, sticky=W) #This one

ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)

outputText = StringVar()
outputText = Label(mainframe, textvariable=_convertOutput).grid(column=3, row=2, sticky=W)

ttk.Button(mainframe, text="Reverse", command=reverse).grid(column=1, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

_input_entry.focus()
root.bind("<Return>", calculate)
root.bind("<Shift_L>", reverse)

root.mainloop()