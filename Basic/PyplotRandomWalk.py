import matplotlib.pyplot as plt 
from random import choice
%matplotlib inline

step_option = [1,-1]
step_choice = choice(step_option)
# step_choice

def rand_walk(step_num):
    walk = []
    step_choice = choice([1,-1])
    walk.append(step_choice)
    for i in range(1,step_num):
        step_choice_2 = choice([1,-1])
        next_step = walk[i-1] + step_choice_2
        walk.append(next_step)
    return walk  

random_w = rand_walk(100)
print(random_w)

plt.plot(random_w)
plt.xlabel('Number of Steps')
plt.ylabel('Distance from Origin')
plt.title('Our Random Walk')
plt.show()
