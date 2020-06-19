import matplotlib.pyplot as plt
import numpy as np
import random
print("Do you want to move? Say yes or no?")
answer = input()
start_pos = int(input("Enter your start position"))
ans = [start_pos]
avg_1 = []
steps = int(input("enter steps"))
prob = []
a = []
for x in range(5):
    if answer == 'yes':
        distance = 0

        p_right = float(input("enter probability to move right"))
        prob.append(p_right)
        for i in range(5):

            p_left = 1-p_right
            path_A, prob_a = [-1, 0, 1], [p_left, 0, p_right]
            for i in range(1, steps+2):
                steps_ahead1 = np.random.choice(path_A, size=1, p=prob_a)
                newposition = ans[-1]+steps_ahead1[0]
                ans.append(newposition)
                # a.append(abs(newposition))
            dist = abs(ans[-1]-ans[0])
            a.append(dist)
        avg = sum(a)/len(a)
        avg_1.append(avg)
        # avg = sum(ans) / len(ans)
        # avg_1.append(avg)

        # plt.plot(avg_1)
    # print(sum(a) / len(a))

    # else:
    #     for i in range(1, steps):

    #         ans.append(start_pos)

    # plt.plot(ans)
    # plt.xlabel("Steps")
    # plt.ylabel("Distance")
    # plt.show()
plt.ylabel("Distance")
plt.xlabel("Probability")
# plt.show()
plt.hist(prob, weights=avg_1, density=False)
plt.show()
