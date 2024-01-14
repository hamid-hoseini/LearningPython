def bubble_sort(my_list):
    swap_again = True
    n = len(my_list)
    while n > 0 and swap_again == True:
        n = n - 1
        swap_again == False
        
        for i in range(n):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swap_again = True
    return my_list        

test_2 = [70,24,87,45,6,3,2,8,5]
print(bubble_sort(test_2))
