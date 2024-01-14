def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        value = my_list[i]
        j = i
        while j > 0 and my_list[j-1] > value:
            my_list[j] = my_list[j-1]
            j = j - 1
        my_list[j] = value
    return my_list  

test_2 = [70,24,87,45,6,3,2,8,5]
print(insertion_sort(test_2))
