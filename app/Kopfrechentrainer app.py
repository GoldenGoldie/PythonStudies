from tkinter import *
from tkinter import ttk


root = Tk()
root.title ("Kopfrechentreiner")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky= (N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

mode = StringVar()
mode_entry = ttk.Entry(mainframe, width=8, textvariable=mode)
mode_entry.grid(column=2, row=2,sticky=(W,E))

calculationsymbol = StringVar()
mode_entry = ttk.Entry(mainframe, width=8, textvariable=calculationsymbol)
mode_entry.grid(column=2, row= 5,sticky=(W,E))

ttk.Label(mainframe, text="which mode do you want:").grid(column=1, row=1,sticky=(W,E))
ttk.Label(mainframe, text="easy, medium, hard").grid(column=1, row=2, sticky=(W,E))
ttk.Label(mainframe, text=" calculationtyp?").grid(column=1, row=4,sticky=(W,E))
ttk.Label(mainframe, text="+,-,*,/").grid(column=1, row=5, sticky=(W,E))
ttk.Label(mainframe, text="").grid(column=1, row=3,sticky=(W,E))



root.mainloop()