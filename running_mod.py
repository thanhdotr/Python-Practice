
i = 0
one  = []
two = []
four = []
def time_for_running(time):
    average_time = 0
    for i in range (0,len(time)):
        print(f"The {i+1}th time record is: {time[i]}")
        average_time += time[i]
    time.sort()
    print(f"The fastest time for a 200m run is {time[0]}")
    print(f"The average time for a 200m run is {average_time/len(time)}:/2f")


while True:
    event = int(input("What is the event that they spend running ? enter the number of m only"))
    i = float(input("What is the time that is required to run the race ?"))
    if i == -1 :
        break
    elif event == 400 :
        four.append(i)

    elif event == 200:
        two.append(i)

    elif event == 100:
        one.append(i)
while True:
    event = int(input("What event will you want to print? (enter 100,200 or 400 or -1"
                      " if you want to end the program)"))
    if event == 100:
        time_for_running(one)
    if event == 200:
        time_for_running(two)
    if event == 400:
        time_for_running(four)
    if event == -1:
        break
    print()
