from tkinter import *
from tkinter import ttk
import random


root = Tk()
root.title ("Kopfrechentreiner")



mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky= (N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

def show():
    ttk.Label(mainframe,text=f"{random.randrange(1,10)} + {random.randrange(1,10)}").grid(column=1, row= 7, sticky=(W,E))
    ttk.Label(mainframe,text=mode).grid(column=2, row= 14, sticky=(W,E))
def random_number_gen():
    try:
        calculationtyp = str(calculationsymbol.get())
        modes = str(mode)



    except ValueError:
        pass

def chechbox_check():
    ttk.Label(mainframe,text="it works").grid(column=1, row=15, sticky=(W,E))
    


         

mode = StringVar()
mode_entry = ttk.Entry(mainframe, width=8, textvariable=mode)
mode_entry.grid(column=2, row=2,sticky=(W,E))

calculationsymbol = StringVar()
calculationsymbol_entry = ttk.Entry(mainframe, width=8, textvariable=calculationsymbol)
calculationsymbol_entry.grid(column=2, row= 5,sticky=(W,E))

ttk.Label(mainframe, text="which mode do you want:").grid(column=1, row=1,sticky=(W,E))
ttk.Label(mainframe, text="you can chose these modes: easy, medium, hard    ").grid(column=1, row=2, sticky=(W,E))
ttk.Label(mainframe, text=" calculationtyp?").grid(column=1, row=4,sticky=(W,E))
ttk.Label(mainframe, text="you can choose these calcuationsymbols:+,-,*,/").grid(column=1, row=5, sticky=(W,E))
ttk.Label(mainframe, text="").grid(column=1, row=3,sticky=(W,E))



def trystuff():
    ttk.Label(mainframe, text=calculationsymbol).grid(column=1, row=9, sticky=(W,E))


ttk.Button(mainframe, text="show calculation",command=show).grid(column=3, row=7, sticky=(W,E))
ttk.Button(mainframe, text="try", command=random_number_gen).grid(column=2, row=9, sticky=(W,E))

x = ttk.Checkbutton(root, text= "easy",command=chechbox_check,onvalue="modes",offvalue= "other modes").grid(column=1, row= 13,sticky=(W,E))




root.mainloop()