import random

print("what do you want to learn?")

while(True):
    calculation = (input("Show me the calculation symbol: "))
    
    control_1 = False

    if calculation == "end":
        break

    if calculation == "*":
        number_1 = random.randrange(1,10)
        number_2 = random.randrange(1,20)
        calculate = (number_1* number_2)
        print (f" { number_2 } * {number_1}")
        control_1 = True   

    if calculation == "+":
        number_1 = random.randrange(20,150)
        number_2 = random.randrange(20,150)
        calculate = (number_1 + number_2)
        print(f"{number_1} + {number_2}")
        control_1 = True

    if calculation == "-":
        number_1 = random.randrange(20,150)
        number_2 = random.randrange(20,75)
        calculate = (number_1 - number_2 )
        print(f"{number_1} - {number_2}")
        control_1 = True

    if calculation == "/":
        number_1 = random.randrange(25,150)
        number_2 = random.randrange(2,25)
        calculate = (number_1 / number_2)
        print(f"{number_1} / {number_2}")
        control_1 = True
    
    if control_1 == False:
        print("nice try")
        print("don't try this again!")
        control_1 = False
    
    if control_1:
        
        result_human = (input("What is your result?"))      

        result_human_1 = int(result_human)  
        
             
        if result_human == calculate  :
                print ("correct")
                control_1 = True

        if result_human != calculate  :
                print("wrong")
                print(calculate)
                control_1 = True
        
