def linear_search(item, my_list):
    i = 0 
    found = False
    
    while i < len(my_list) and found == False:
        if my_list[i] == item:
            found = True
        else:
            i = i + 1
    return found     


test = [6,5,8,2,3,45,87,24,70]
print(linear_search(4,test))
print(linear_search(88,test))
