
timerdurationsymbol = "h"

def CheckIfIsDigit(I):
    if I.isdigit():
        return int(I)
    else:
        return "no number"
    
def timesymbol(I):
    if I == "sec" or I == "s":
        return 1
    if I == "min" or I == "m":
        return 60 
    if I == "hour" or I == "h":
        return 3600

def Checkiftimesymbol(I):
    I = timerdurationsymbol
    Y = CheckIfIsDigit(I)

    if Y == "no number":
        I = timesymbol(I)
        return I
    
timerdurationsymbol = Checkiftimesymbol(timerdurationsymbol)

print(timerdurationsymbol)