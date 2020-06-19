import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib as mpl

steps_list = []
avg_list = []

for s in range(10000):

    if s % 100 == 0:
        print(s)

    R = 20

    x, y = 0, 0
    x, y = 0, 0
    Pi = math.pi
    p1 = np.random.uniform(0, Pi * R * R)
    p2 = np.random.uniform(0, Pi * R * R)
    # the point value here is the area of the point. So we can get the radius of it:
    p1 = math.sqrt(p1 / Pi)
    p2 = math.sqrt(p2 / Pi)
    # Then we can use polar coordinate to get the final answer:
    angle = np.random.uniform(0, 2 * Pi)
    angle2 = np.random.uniform(0, 2 * Pi)
    x1 = x + p1 * math.cos(angle)
    y1 = y + p1 * math.sin(angle)

    x2 = x + p2 * math.cos(angle2)
    y2 = y + p2 * math.sin(angle2)




    #fig, ax = plt.subplots()
    steps = random.randint(10, 100)
    steps_list.append(steps)

    personA = []  # personA[i] is the position of i_th person on point A
    personB = []  # personB[i] is the position of i_th person on point B
    for i in range(100):
        personA.append((x1, y1))
        personB.append((x2, y2))

    meetings = []
    for j in range(steps):

        meetings.append(0)  # stores number of meetings occured in the j_th step

        # move all persons by one step

        for i in range(100):

            x, y = personA[i]

            r = np.random.uniform(0, 1)
            Theta = np.random.uniform(0, 360)
            Theta = Theta * (math.pi/180)
            dx = r * math.cos(Theta)
            dy = r * math.sin(Theta)
            if (x+dx)**2 + (y+dy)**2 >= R**2:
                x = x - dx
                y = y - dy
            else:
                x = x + dx
                y = y + dy
            personA[i] = (x, y)

            x, y = personB[i]
            r = np.random.uniform(0, 1)
            Theta = np.random.uniform(0, 360)
            Theta = Theta * (math.pi/180)
            dx = r * math.cos(Theta)
            dy = r * math.sin(Theta)
            if (x+dx)**2 + (y+dy)**2 >= R**2:
                x = x - dx
                y = y - dy
            else:
                x = x + dx
                y = y + dy
            personB[i] = (x, y)

        # check if any person A has meet any person B in this step

        for a in range(100):
            for b in range(100):
                x1, y1 = personA[a]
                x2, y2 = personB[b]
                if (x1-x2)**2 + (y1-y2)**2 <= 1:
                    meetings[j] = meetings[j] + 1


    avg = 0
    if sum(meetings) > 0:
        for i in range(steps):
            avg = avg + i*meetings[i]
        avg = avg/sum(meetings)
    avg_list.append(avg)


plt.hist(steps_list, weights=avg_list, density=True)
plt.xlabel("Time")
plt.ylabel("Average Number of steps")
plt.show()

