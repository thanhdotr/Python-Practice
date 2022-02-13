i = 0
time = []
average_time = 0
while True:

    i = float(input("What is the time that is required to run a 200m race ?"))
    if i == -1 :
        break

    else:
        time.append(i)

for i in range (0,len(time)):
    print(f"The {i+1}th time record is: {time[i]}")
    average_time += time[i]
time.sort()
print(f"The fastest time for a 200m run is {time[0]}")
print(f"The average time for a 200m run is {average_time/len(time)}")
