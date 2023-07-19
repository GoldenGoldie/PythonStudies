import time

fisch = True

Endergebniss_2 = 0

while (fisch):

    

    Ergebniss_1 = time.time()

    input("Hello")

    Ergebniss_2 = time.time()

    Endergebniss = Ergebniss_2 - Ergebniss_1

    Endergebniss = int(Endergebniss)

    Endergebniss_2 = Endergebniss_2 + Endergebniss


    if Endergebniss_2 > 20:
        fisch = False

    print(Endergebniss)