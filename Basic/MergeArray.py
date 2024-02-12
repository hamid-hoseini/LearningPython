def merge_arrray(arrayA, arrayB):
  # 1: Merge arrayA and arrayB
  # 2: Remove dublicates
  # 3: sort the result
  return sorted(set(arrayA + arrayB))

a = [2, 3, 5, 7, 9]
b = [3, 5, 6, 8, 10]
c = merge_array(a, b)
print (c)

# output: [2, 3, 5, 6, 7, 9, 10]
