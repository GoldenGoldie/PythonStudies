symbol = input("was willst du rechnen?")

zahl1 = int(input("nenne eine Zahl:"))

zahl2 = int(input("noch eine Zahl:"))
if symbol == "+":
    x = (zahl1 + zahl2)

if symbol == "-":
    x = (zahl1 - zahl2)

if symbol == "*":
    x = (zahl1 * zahl2)

if symbol == "/":
    x = (zahl1 / zahl2)

print("Das Ergebniss ist:",x)