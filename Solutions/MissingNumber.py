'''
You have been provided with the list of positive integers from 1 to n. All the numbers from 1 to n are present except x, and you must find x. 
Example:
4 5 3 2 8 1 6

n = 8 
missing number = 7
'''

def find_missing(input_list):

  sum_of_elements = sum(input_list)
 
  # There is exactly 1 number missing
  n = len(input_list) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
 
  return int(actual_sum - sum_of_elements)
list_1 = [1,5,6,3,4]


find_missing(list_1)
# 2
