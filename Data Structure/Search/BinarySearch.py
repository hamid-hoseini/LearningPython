def binary_search(item, my_list):
    found = False
    first = 0
    last = len(my_list) - 1
    
    while first <= last and found == False:
        midpoint = (first + last)//2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found            


test = [2,3,5,6,8,24,45,70,87]
print(binary_search(87,test))
print(binary_search(88,test))
