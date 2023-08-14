import random

calculationsymbol = input ("hello")

calculate = 0

number_1 = random.randrange(1,15)

number_2 = random.randrange(1,5)

c = 0

def Calculation():
    if calculationsymbol == "+":
       return number_1 + number_2 
        
    if calculationsymbol == "-":
        i = number_1 - number_2

    if calculationsymbol == "*":
        i = number_1 * number_2

    if calculationsymbol == "/":
        i = number_1 / number_2 


c = Calculation()

print(c)

