"""
When moving 3 disks from A to C, we move the top two disks to B and then the bottom disk to C. 
More generally, when moving n disks from A to C we move n-1 disks to B; we then move the base 
disk from A to C and then move the stack of n-1 on B to C .
We have 3 towers A, B and C or 3 Stacks
"""

A = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
B = []
C = []
# According to our rules, if we want to move all disks 3,2 and 1 from A to C, we first move two disks from A to B. We then move
# the base disk from A to C and then the stack of two from B to C
count = 0
def towers_of_hanoi(A,B,C,n):
    global count 
    
    if n == 1:
        disk = A.pop()
        C.append(disk)
        count +=1    
    else:
        
        towers_of_hanoi(A,C,B,n-1)
        
        towers_of_hanoi(A,B,C,1)
        
        towers_of_hanoi(B,A,C,n-1)
    return count   
       
towers_of_hanoi(A,B,C,14)

