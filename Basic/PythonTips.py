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
