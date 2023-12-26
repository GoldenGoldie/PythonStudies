from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk
root.title = "Kopfrechentrainer"

mainframe = ttk.Frame("3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
