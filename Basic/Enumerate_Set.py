### Enumerate
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alphabet)

#alpha_list
for char in alpha_list:
    print(char)    


for i in range(len(alpha_list)):
    print(i,alpha_list[i])
    
for count, item in enumerate(alpha_list):
    print(count,item)
for count, item in enumerate(alpha_list, start = 12):
    print(count,item)

A = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
B = [6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14]
A = set(A)
A
B = set(B)
B
A & B # Intersection
A | B # Union
A - B # Difference
A ^ B # Symmetric Difference
z = None
