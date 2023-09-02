import random

mode = input("hello1")

calculationsymbol = input("hello2")

if calculationsymbol == "suaring":
    calculationsymbol = "*"

def numbergenerator():
    if mode == "easy":

        

        if calculationsymbol == "+" or "-":
            number_1 = random.randrange(10,50)
            

        if calculationsymbol == "*":
            number_1 = random.randrange(1,25)
    

        if calculationsymbol == "/":
            number_1 = random.randrange(1,25)


    if mode == "medium":
        if calculationsymbol == "+" or "-":
         number_1 +=  random.randrange(100,200)

        if calculationsymbol == "*":
            number_1 = random.randrange(10,25)

        if calculationsymbol == "/":
            number_1 = random.randrange(10,100)

    if mode == "hard":
        if calculationsymbol == "+" or "-":
            number_1 += random.randrange(50,500)
        
        if calculationsymbol == "*":
            number_1 = random.randrange(25,150)
        
        if calculationsymbol == "/":
            number_1 = random.randrange(50,500)
        
    return number_1



x = numbergenerator()

y = numbergenerator()

if calculationsymbol == "squaring":
    y = x

print(x)