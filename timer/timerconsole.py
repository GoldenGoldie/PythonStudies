import time

count = True

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


    
    
input = input("how long should the timer go ?")

timeramount = input.split()

timernumber = timeramount[0]

timernumber = CheckIfIsDigit(timernumber)

timerdurationsymbol = timeramount[1]

timerdurationsymbol = Checkiftimesymbol(timerdurationsymbol)

print(timernumber)

time_start = int(time.time())

timernumber = timernumber * timerdurationsymbol

time_end = time_start + timernumber



while count:
    time_duration = int(time.time())

    if time_end == time_duration:
        print("beep,beep")
        break