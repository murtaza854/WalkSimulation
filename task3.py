import matplotlib.pyplot as plt
import numpy as np
import random
import math
import turtle
 
x, y = 0, 0
fig,ax=plt.subplots()
steps = 100000
lst = []
xlist=[]
ylist=[]
c = 0
R = 100
for j in range(10):
    for i in range(steps + 1):
        r = random.choice([0, 0.5, 1])
        Theta = random.randint(0, 360)
        Theta = Theta * (math.pi/180)
        x += r * math.cos(Theta)
        y += r * math.sin(Theta)
        xlist.append(x)
        ylist.append(y)
        # print(int(math.sqrt((x**2 + y**2))))
        if int(math.sqrt(x**2 + y**2)) >= R:
            x -= r * math.cos(Theta)
            y -= r * math.sin(Theta)
circle1 = plt.Circle((0,0),100,fill=False)

ax.add_artist(circle1)
plt.plot(xlist,ylist)
plt.xlim(-100, 100)
plt.xlabel("distance in x axis")
plt.ylabel("distance in y axis")
plt.ylim(-100, 100)
plt.show()