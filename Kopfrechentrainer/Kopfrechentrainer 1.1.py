import random

import time

finaltime = 0

print("what do you want to learn?")

end_control = True


def Calculation():
        print(f" {number_1} {calculationsymbol} {number_2}")

        if calculationsymbol == "+":
            return  number_1 + number_2 
        
        if calculationsymbol == "-":
            return number_1 - number_2

        if calculation == "*":
            return number_1 * number_2

        if calculationsymbol == "/":
            return number_1 / number_2 
        
        if calculationsymbol == "squaring":
            return number_1 * number_2

def CheckIfIsDigit(i):
    if i.isdigit():
        return int(i)

    return "no Number"


while True:
    control_1 = False

    mode = str(input("Do you want the easy or hard mode or the random mode?"))
    control_2 = False

    if mode == "hard" or mode == "h":
        control_1 = True
        control_2 = True
    if mode == "easy" or mode == "e":
        control_1 = True
        control_2 = True

    if mode == "random" or mode == "r":
        control_1 = True
        control_2 = False
        calculation = "easy"
        mode_2 = "random"

    if control_1 == False:
        print("don't do this!")
    if control_2:
        calculationsymbol = input("Do you want to practice +, -, *, / or squaring you can also choose the random mode and you can stop practicing if you enter end: ")

    if control_1 == False:
        calculationsymbol = "end"

    if calculationsymbol == "end":
        break


    print("How many calculations do you want to do?")

    loop_count = str(input("Between 1 and 10 "))

    loops_control = False

    loops = 0

    loop_count = CheckIfIsDigit(loop_count)

    if loop_count in range(1, 10):
        control_1 = True
        loops_control = True

    if control_1 == False:
        loops_control = False
        print("Do not do this!")


    while loops_control:

        time_1 = time.time()

        if mode == "random":
            random_1 = random.randrange(1, 3)

            random_2 = random.randrange(1, 6)

            if random_1 == 1:
                mode = "easy"

            if random_1 == 2:
                mode = "hard"

            if random_2 == 1:
                calculationsymbol = "+"

            if random_2 == 2:
                calculationsymbol = "-"

            if random_2 == 3:
                calculationsymbol = "*"

            if random_2 == 4:
                calculationsymbol = "/"

            if random_2 == 5:
                calculationsymbol = "squaring"

            control_1 = True

        if mode == "easy":
            if calculationsymbol == "*":
                number_1 = random.randrange(1, 10)
                number_2 = random.randrange(1, 20)
                control_1 = True

            if calculationsymbol == "+":
                number_1 = random.randrange(20, 150)
                number_2 = random.randrange(20, 150)
                control_1 = True

            if calculationsymbol == "-":
                number_1 = random.randrange(20, 150)
                number_2 = random.randrange(20, 75)
                control_1 = True

            if calculationsymbol == "/":
                number_1 = random.randrange(25, 150)
                number_2 = random.randrange(2)
                control_1 = True

            if calculationsymbol == "squaring":
                number_1 = random.randrange(1, 10)
                number_2 = number_1
                control_1 = True

        if mode == "hard":
            if calculationsymbol == "+":
                number_1 = random.randrange(50, 500)
                number_2 = random.randrange(110, 700)
                control_1 = True

            if calculationsymbol == "-":
                number_1 = random.randrange(25, 500)
                number_2 = random.randrange(25, 700)
                control_1 = True

            if calculationsymbol == "*":
                number_1 = random.randrange(25, 150)
                number_2 = random.randrange(2, 25)
                control_1 = True

            if calculationsymbol == "/":
                print("You only have to write the first numbers in front")
                number_1 = random.randrange(50, 500)
                number_2 = random.randrange(2, 20)
                control_1 = True

            if calculationsymbol == "squaring":
                number_1 = random.randrange(10, 30)
                number_2 = number_1
                control_1 = True

        calculate = Calculation()

        if control_1 == False:
            print("nice try")
            print("don't try this again!")
            control_1 = False

        if control_1:
            result_human = input("What is your result?")

            result_human_1 = str(result_human)

            calculate_2 = str(calculate)

            control_1 = False

            if result_human == calculate_2:
                print("correct")
                control_1 = True
                

            if result_human_1 != calculate_2:
                print("wrong")
                print(calculate_2)
                control_1 = True

            time_2 = time.time()

            endtime = time_2 - time_1

            print(f"you did it in  {endtime} maxis")

            finaltime = endtime + finaltime

            

            loops += 1

            loops_control = loop_count != loops

        if loops_control == False:
            end_control = False
            print(f"your final time is {finaltime}")

