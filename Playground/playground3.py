import random
def numbergenerator():


    if mode == "easy" or mode == "e" :

        if t == 0:
            
            if calculationsymbol == "+" or calculationsymbol == "-":
                number_1 = random.randrange(10,50)

            if calculationsymbol == "*" or calculationsymbol == "squaring":
                number_1 = random.randrange(1,25)

            if calculationsymbol == "/":
                number_1 = random.randrange(1,25)




        if t == 1:

            if calculationsymbol == "/":
                number_1 = 2


    if mode == "medium" or mode == "m":
            
        if t == 0:
            if calculationsymbol == "+" or "-":
                number_1 =  random.randrange(100,200)

            if calculationsymbol == "*":
                number_1 = random.randrange(10,25)

            if calculationsymbol == "/":
                number_1 = random.randrange(10,100)

        if t == 1:
          number_1 = random.randrange(2,10)

    if mode == "hard" or mode == "h" :
            
        if t == 0:

            if calculationsymbol == "+" or "-":
                number_1 = random.randrange(50,500)
        
            if calculationsymbol == "*":
                number_1 = random.randrange(25,50)
        
            if calculationsymbol == "/":
                number_1 = random.randrange(50,500)

        if t == 1:
            number_1 = random.randrange(2,25)
        
    return  number_1



f = True
while f:

    mode = input("hello1")

    calculationsymbol = input("hello2")

    t = 0
    

    x = numbergenerator()
    if calculationsymbol == "/":
     t = 1
     f = 1

    y = numbergenerator()

    if calculationsymbol == "squaring":
        y = x

    if mode == "end":
        break

    print(x,y)