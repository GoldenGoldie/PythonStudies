def checknumber(i):
    if i.isdigit():
        return float(i)
    else:
        return "no number"
    

daysleft = input("how many days are left until the exam")

time_day = input("how much time do you want to invest (in hours)?")

daysleft = checknumber(daysleft)

time_day = checknumber(time_day)

if daysleft != "no number" or time_day != "no number":
    timedayminutes = time_day * 60
else:
    timedayminutes = "no number"
    
counter = 0.0

easy_task = 5

mid_task = 30

hard_task = 45


while True:
    
    if timedayminutes == "no number":
        break


    amount_hard_task = int(timedayminutes / hard_task)
    timeday = timedayminutes - (hard_task * amount_hard_task)

    amount_mid_task = int(timeday / mid_task)
    timeday = timeday - (mid_task * amount_mid_task)

    amount_easy_task = int(timeday / easy_task)
    timeday = time_day - (easy_task *amount_easy_task)

    counter += 1

    print(f"day{counter}")
    print(f"{amount_hard_task}hard tasks")
    print(f"{amount_mid_task} medium tasks")
    print(f"{amount_easy_task} easy tasks")

    if counter == daysleft:
        break
