from tkinter import *
import tkinter as tk
from tkinter import ttk
import random

def correct():
    correct_result.set(int(x + y))
    

def calculation_numbergenerator(i):

    if i == 0:
        number_1 = random.randrange(1,10)

    if i == 1:
        number_1 = random.randrange(10,20)

    return number_1

x = 0
y = 1

x = calculation_numbergenerator(x)
y = calculation_numbergenerator(y)


root = Tk()
root.title("Kopfrechentrainer")

mainframe = ttk.Frame(root,padding= "3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N, W, E, S))

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

#Entry Widget
human_result = StringVar()
human_result_entry = ttk.Entry(mainframe, width=8, textvariable=human_result)
human_result_entry.grid(column=2, row=2, sticky=(W,E))

#Right result
correct_result = StringVar()
ttk.Label(mainframe, textvariable=correct_result).grid(column=2,row=3,sticky=(W,E))

#Button 
ttk.Button(mainframe,text="correcture", command=correct()).grid(column=3, row= 3, sticky=(W,E))

#Text
ttk.Label(mainframe,text="your result:").grid(column=1, row=2, sticky=(W,E))
ttk.Label(mainframe,text="the calculation:").grid(column=1, row=1, sticky=(W,E))
ttk.Label(mainframe, text=f"{x} + {y}").grid(column=2,row=1,sticky=(W,E))


human_result_entry.focus()
root.bind("<Return>", correct)

root.mainloop()