''' Create a program that works out the total time of a triathlon and awards depending on total time taken'''
print("Welcome to the Ultimate Triathlon awards notification app" "\n")

name = (input("What is your name? "))
swim = int(input("Please enter the total time in minutes the swimming event took you. "))
cycle = int(input("Please enter the total time in minutes the cycling event took you. "))
run = int(input("Please enter the total time in minutes the running event took you. "))
mins = ("minutes.")
time = (swim + cycle + run)     # total time of all 3 events 

award1 = ("Provincial Colours award")           # under 100 mins
award2 = ("Provincial Half Colours award")      # under 105 mins
award3 = ("Provincial Scroll award")            # under 110 mins
no_award = ("We thank you for your effort, but no award on this occasion as your time was over 111 minutes")


total_time = (", Congratulations your total time was")
sad_time = (", your time was")
acheive = ("This has acheived a")

# time vs award calculations below
if time <= 100:
    print(name + total_time, time, mins, acheive, award1)
elif time >= 101 and time <= 105:
    print(name + total_time, time, mins, acheive, award2)
elif time >= 106 and time <=110:
    print(name + total_time, time, mins, acheive, award3)
else:
    print(name + sad_time, time, mins, no_award)    