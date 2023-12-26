from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

root = Tk()
root.title ("Kopfrechentreiner")

calculations_result_easy = 1
human_result_easy = 1


mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky= (N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

def easy_calculations():
    clalculations_sign = random.randrange(1,5)

    if clalculations_sign == 1 or clalculations_sign == 2:
        easy_number1 = random.randrange(10,20)
        easy_number2 = random.randrange(1,11)

        if clalculations_sign == 1:
            clalculations_sign = "+"
            clalculations_result = easy_number1 + easy_number2
        
        if clalculations_sign == 2:
            clalculations_sign = "-"
            clalculations_result = easy_number1 - easy_number2

    if clalculations_sign == 3 or clalculations_sign == 4:
        easy_number1 = random.randrange(2,20)
        easy_number2 = 2

        if clalculations_sign == 3:
            clalculations_sign = "*"
            clalculations_result = easy_number1 * easy_number2

        if clalculations_sign == 4:
            clalculations_sign = "/"
            clalculations_result = int(easy_number1 / easy_number2)
            
    
    ttk.Label(mainframe,text=(f"{easy_number1} {clalculations_sign} {easy_number2}")).grid(column=1,row=2,sticky=(W,E))
    ttk.Label(mainframe,text="your result:").grid(column=2,row=2,sticky=(W,E))
    return clalculations_result
    

  
    
    


def medium_calculations():
    print(human_result_easy)
    

def hard_calculations():
    print("f")
    print(checkbox_easy)


def calculation_result_correctur():
        ttk.Label(mainframe,text=f" is correct").grid(column=5,row=2,sticky=(W,E))

ttk.Label(mainframe,text="").grid(column=2,row=2,sticky=(W,E))

checkbox_easy = tk.StringVar()
checkbox_medium = tk.StringVar()


calculations_result_easy = tk.StringVar


calculations_result_easy = ttk.Checkbutton(mainframe, text= "easy",variable=checkbox_easy,command=easy_calculations, onvalue="easy",offvalue= "no easy").grid(column=1,row=1,sticky=(W,E))


ttk.Checkbutton(mainframe, text="medium",command=medium_calculations,variable= checkbox_medium,onvalue="medium", offvalue="no medium").grid(column=1,row=3,sticky=(W,E))

ttk.Checkbutton(mainframe,text="test",command=hard_calculations).grid(column=1,row=5,sticky=(W,E))



human_result_easy = StringVar()
human_result_easy_entry = ttk.Entry(mainframe,width=10,textvariable=human_result_easy)
human_result_easy_entry.grid(column=3,row=2,sticky=(W,E))



ttk.Button(mainframe,text="compare",command = calculation_result_correctur).grid(column=4,row=2,sticky=(W,E))



root.mainloop()


