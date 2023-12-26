import time

count = True

timeaumount = int(input("how long should the timer go (in seconds)?"))

time_start = int(time.time())

time_end = time_start + timeaumount

while count:
    time_duration = int(time.time())

    if time_end == time_duration:
        print("beep,beep")
        break