import random

print("what do you want to learn?")

end_control = True

while(True):
    control_1 = False

    

    mode = str(input("Do you want the easy or hard mode or the random mode?"))
    control_2 = False

    if mode == "hard":
         control_1 = True
         control_2 = True
    if mode == "easy":
         control_1 = True
         control_2 = True

    if mode == "random":
        control_1 = True
        control_2 = False
        calculation = "easy"
        mode_2 = "random"

    if control_1 == False:
         print ("don't do this!")
    if control_2:
        calculation = (input("Do you want to practice +, -, *, / or squaring you can also choose the random mode and you can stop practicing if you enter end: "))

    if control_1 == False:
     calculation = "end"    
        
    print("How many calculations do you want to do?")

    loop_count = str(input("Between 1 and 10 "))
        
    loops_control = False

    loops = 0

        

    if loop_count == "1":
            loop_count = 1
            control_1 = True
            loops_control = True

    if loop_count == "2":
            loop_count = 2
            control_1 = True
            loops_control = True
        
    if loop_count == "3":
            loop_count = 3

            control_1 = True
            loops_control = True
        
    if loop_count == "4":
            loop_count = 4
            control_1 = True
            loops_control = True

    if loop_count == "5":
            loop_count = 5
            control_1 = 1 
            loops_control = True

    if loop_count =="6":
            loop_count = 6 
            control_1 = True
            loops_control = True

    if loop_count =="7":
            loop_count = 7
            control_1 = True
            loops_control = True

    if loop_count == "8":
            loop_count = 8
            control_1 = True
            loops_control = True

    if loop_count ==  "9":
            loop_count = 9
            control_1 = True
            loops_control = True

    if loop_count =="10":
            loop_count = 10
            control_1 = True
            loops_control = True

        
    if control_1 == False:
            loops_control = False 
            print ("Do not do this!")
                               
    if calculation == "end":
           break
    
    if mode == "random":
         mode_2 = "random"
         calculation = "+"



    if mode == "easy":
         mode_2 = "easy"
    
    if mode == "hard":
         mode_2 = "hard"
        
        

    while(loops_control):
            

            if mode_2 == "random":
                random_1  = random.randrange(1,3)

                random_2 = random.randrange(1,6)

                if random_1 == 1:
                 mode = "easy"

                if random_1 == 2:
                 mode = "hard"

                if random_2 == 1:
                 calculation = "+"

                if random_2 == 2:
                 calculation = "-"

                if random_2 == 3:
                 calculation = "*"

                if random_2 == 4:
                 calculation = "/"

                if random_2 == 5:
                 calculation = "squaring"
                    
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

                loops += 1

                loops_control = (loop_count != loops )

                

                

            if loops_control == False:
                end_control = False
                