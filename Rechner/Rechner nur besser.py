symbol=(input("was willst du rechnen?:"))
rechnung = symbol.split()
x = 1

zahl1 = int(rechnung[0])

zahl2 = int(rechnung[2])

if rechnung[1] == "+":
    x = (zahl1 + zahl2)

if rechnung[1] == "-":
    x = zahl1 - zahl2

if rechnung[1] == "*":
    x = zahl1 * zahl2

if rechnung[1] == "/":
    x = zahl1 / zahl2

print("Das Ergebniss ist:",x)