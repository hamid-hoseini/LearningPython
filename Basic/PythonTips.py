# Here you can find some important tips in Python

# Tip 1:
m = []
for x in range(1, 11):
  m.append(x**2)
print m

# The above code is equivalent to:
m = [x**2 for x in range(1, 11)]

"""
Result:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

# Tip 2:

''' using * means we don't know how many values will be passed to the function '''
def calc_mean(first, *remainder)
  mean = (first + sum(remainder)) / (1 + len(remainder))
  print (mean)
  return mean

calc_mean(6, 10, 3, 5 , 2, 1)

