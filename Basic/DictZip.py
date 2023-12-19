'''
Question 3
Create a dictionary to represent the open, high, low, close share price data 
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
key_names = ['Open','High','Low','Close']
prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]

d_1 = {}

for i in range(len(key_names)):
   d_1[companies[i]] = dict(zip(key_names,prices[i]))
       
print(d_1)   


# Result:
# {'Python DS': {'Open': 12.87, 'High': 13.23, 'Low': 11.42, 'Close': 13.1}, 
#  'PythonSoft': {'Open': 23.54, 'High': 25.76, 'Low': 21.87, 'Close': 22.33}, 
#  'Pythazon': {'Open': 98.99, 'High': 102.34, 'Low': 97.21, 'Close': 100.065}, 
#  'Pybook': {'Open': 203.63, 'High': 207.54, 'Low': 202.43, 'Close': 205.24}
# }
