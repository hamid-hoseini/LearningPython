# Create a list of n coins
n = 1001
coins = [0]*n
#The first loop increases the step size, the second iterates through the coins using that step size, swapping a 1 for a 0 or a 0 for a 1.  This is a convenient way of switching between those two values. In this case 1 indicates 'Head' and 0 'Tail'.
for i in range(1,n):
    for j in range(0,n,i):
        coins[j] = 1 - coins[j]
       
#We create a dictionary, the key is the index value of the list of coins, the value is heads.
d = {}
for i,v in enumerate(coins):
    if v != 0:
        d[i]=v
        
d
# Can you see the pattern?
L = []
for k,v in d.items():
    L.append(k)
print(L)
import math
L2 = [math.sqrt(num) for  num in L]

