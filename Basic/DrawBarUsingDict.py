'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should 
be random numbers created from the random module. Can you draw a bar graph of 
the results?
'''

import random
import matplotlib.pyplot as plt

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = dict()

for letter in keys:
   d[letter] = random.randint(1,100)
   
print(d)    

# zip(*d.items() returns two tuples from values of letter dictionary  
x,y = zip(*d.items()) 

plt.bar(x,y)

