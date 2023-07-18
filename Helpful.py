a = "hallo"
b = "23"
c = "1b"

def CheckIfIsDigit(i):
    if(i.isdigit()):
        return float(i)
    return "no Number"
    

print(CheckIfIsDigit(a))
print(CheckIfIsDigit(b))
print(CheckIfIsDigit(c))