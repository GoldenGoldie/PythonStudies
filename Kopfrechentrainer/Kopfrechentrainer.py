import random

print("what do you want to learn?")

while(True):
    calculation = (input("show me the calculation symbol"))

    if calculation == "end":
        break

    if calculation == "*":
        number_1 = random.randrange(1,10)
        number_2 = random.randrange(1,20)
        calculate = (number_1* number_2)
        print (f" { number_2 } * {number_1}")

    if calculation == "+":
        number_1 = random.randrange(20,150)
        number_2 = random.randrange(20,150)
        calculate = (number_1 + number_2)
        print(f"{number_1} + {number_2}")

    if calculation == "-":
        number_1 = random.randrange(20,150)
        number_2 = random.randrange(20,75)
        calculate = (number_1 - number_2 )
        print(f"{number_1} - {number_2}")

    if calculation == "/":
        number_1 = random.randrange(25,150)
        number_2 = random.randrange(2,25)
        calculate = (number_1 / number_2)
        print(f"{number_1} / {number_2}")

    result_human = int(input("what is your result?"))

    if result_human == calculate  :
        print ("right")

    if result_human != calculate  :
        print("wrong")
        print(calculate)
