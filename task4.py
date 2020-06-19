import matplotlib.pyplot as plt
import numpy as np
import random
# print("Do you want to move? Say yes or no?")
# answer = np.random.choice([0,1])
# start_pos = int(input("Enter your start position"))
ans = [0]
# steps = int(input("enter steps"))
# if answer>0: 
distance = 0
start_pos=0

# p_right = float(input("enter probability to move right"))

# p_left = 1-p_right
avg_list = []
step_list = []
for x in range(5):
    steps = int(input("Enter steps: "))
    a = []
    
    step_list.append(steps)
    for j in range(1000):
        ans = [0]
        distance=0
        dist_list1 = []
        for i in range(1, steps):
            # if np.random.uniform([0, 1]):
            outcome= np.random.uniform(0.0, 1.0, size=1)
            val= ans[i-1] + outcome[0]
            ans.append(val)
            
            #a.append(distance)
        a.append(ans[-1])
    avg=sum(a)/len(a)
    avg_list.append(avg)
    print(avg)
##    dist_list1.append(distance)
##    avg1 = sum(dist_list1) / len(dist_list1)
##    avg = sum(ans) / len(ans)
##    a.append(avg)
##    dist_list.append(avg1)
##aver = sum(ans) / steps


# plt.plot(ans)
plt.xlabel("Steps")
plt.ylabel("Distance")
plt.hist(step_list, weights=avg_list , density=False)
plt.show()
# else:
#     for i in range(1, steps):
 
#         ans.append(start_pos)
 
#     plt.plot(ans)
#     plt.show()
