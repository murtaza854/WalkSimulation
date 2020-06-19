import matplotlib.pyplot as plt
import numpy as np
import random
import time
import matplotlib as mpl


def person1(start_pos1, start_pos2, p1_right, p2_right):
    ans1 = [start_pos1]
    ans2 = [start_pos2]
    x1 = start_pos1
    x2 = start_pos2
    steps = 0
    # x1 = 0
    # x2 = 0
    distance_1 = 0
    distance_2 = 0
    p1_left = 1-p1_right
    p2_left = 1-p2_right
    path_A,prob_a= [-1,0,1],[p1_left, 0,p1_right]
    path_B,prob_b= [-1,0,1],[p2_left, 0,p2_right]
    counter=0
    while True:
        counter += 1
        steps_ahead1 = np.random.choice(path_A,size=1,p=prob_a)
        steps_ahead2 = np.random.choice(path_B,size=1,p=prob_b)
        newposition1=ans1[-1]+steps_ahead1[0]
        newposition2 = ans2[-1] + steps_ahead2[0]
        steps += 1
        ans1.append(newposition1)
        ans2.append(newposition2)
        # print(newposition1, newposition2)
        if newposition1 == newposition2:
            return steps
        if counter == 1000000:
            break
            

        # plt.plot(ans1, c="red")
        # plt.plot(ans2, c="blue")
        # return ans1, ans2
        # plt.xlabel("Steps")
        # plt.ylabel("Distance")
        # plt.show()
print("Do you want to move? Say yes or no?")


p1_right = float(input("enter probability to move right"))
p2_right = float(input("enter probability to move right"))

diff_list = []
avglist=[]
for i in range(5):
    print(i)
    steps_list = []
    start_pos1 = int(input("Enter Position Person 1: "))

    start_pos2 = int(input("Enter Position Person 2: "))
    diff = abs(start_pos1 - start_pos2)
    for j in range(1000):
        
        steps = person1(start_pos1, start_pos2, p1_right, p2_right)
        if steps != None:
            print("pass")
            
            steps_list.append(steps)
    avg=sum(steps_list)/len(steps_list)
    avglist.append(avg)
    diff_list.append(diff)

    # avg1 = sum(ans1) / len(ans1)
    # avg2 = sum(ans2) / len(ans2)
    # avg_list_1.append(avg1)
    # avg_list_2.append(avg2)
    # print(steps)
# person1("blue")

# plt.plot(avg_list_1, c="red")
# plt.plot(avg_list_2, c="blue")
# print(steps)
# for i in range(len(steps)):
#     mpl.pyplot.hist(steps[i], weights=t[i])
plt.hist(diff_list, weights=avglist , density=False)
plt.xlabel("x units apart")
plt.ylabel("time")
plt.show()
