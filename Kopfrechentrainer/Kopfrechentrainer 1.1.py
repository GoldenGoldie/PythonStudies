import random

print("what do you want to learn?")

while(True):
    control_1 = False

    mode = str(input("Do you want the easy or hard mode?"))
    if mode == "hard":
         control_1 = True
    
    if mode == "easy":
         control_1 = True

    if control_1 == False:
         print ("don't do this!")
    if control_1:
        calculation = (input("Do you want to practice +, -, *, / or squaring: "))
    
    
                               
        if calculation == "end":
           break
    

        if mode == "easy":
     
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
                number_2 = random.randrange(2)
                calculate = (number_1 / number_2)
                print(f"{number_1} / {number_2}")
                control_1 = True

            if calculation == "squaring":
                number_1 = random.randrange(1,10)
                number_2 = number_1
                calculate = (number_1 * number_2)
                print(f"{number_1} * {number_2}")
                control_1 = True
    
        if mode == "hard":
         
            if calculation == "+":
              number_1 = random.randrange(50, 500)
              number_2 = random.randrange(110,700)
              calculate = (number_1 + number_2)
              print(f"{number_1} + {number_2}")
              control_1 = True
        
            if calculation == "-":
             number_1 = random.randrange(25,500)
             number_2 = random.randrange(25,700)
             claculate = (number_1 - number_2)
             print(f"{number_1} - {number_2}")
             control_1 = True

            if calculation == "*":
             number_1 = random.randrange(25,150)
             number_2 = random.randrange(2,25)
             calculate = (number_1 * number_2)
             print(f"{number_1} * {number_2}")
             control_1 = True

            if calculation == "/":
             print("You only have to write the first two numbers")
             number_1 = random.randrange(50,500)
             number_2 = random.randrange(2,20)
             claculate = (number_1 / number_2)
             print(f"{number_1} / {number_2}")   
             control_1 = True      

            if calculation == "squaring":
                number_1 = random.randrange(10,30)
                number_2 = number_1 
                calculate = (number_1 * number_2)
                print(f"{number_1} * {number_2}")
                control_1 = True
        
    

    if control_1 == False:
        print("nice try")
        print("don't try this again!")
        control_1 = False
    
    if control_1:
        
        result_human = (input("What is your result?"))      

        result_human_1 = str(result_human)  
        
        calculate_2 = str(calculate)

        control_1 = False

        if result_human == calculate_2  :
                print ("correct")
                control_1 = True

        if result_human_1 != calculate_2:
             print("wrong")
             print(calculate_2)
             control_1 = True

        
        
