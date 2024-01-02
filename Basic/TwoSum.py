# Two Sum problem

def two_sum(nums, target):
        d = {}
        
           
        for i in range(len(nums)):    
            if target - nums[i] in d:
                print(d)
                return [d[target-nums[i]],i]
            
            d[nums[i]] = i
            
        return -1


L = [8,6,11,3]
print(two_sum(L,9))

# result:
# {8: 0, 6: 1, 11: 2}
#[1, 3]

L2 = [2,5,3,7,4]
print(two_sum(L2,10))

#result:
# {2: 0, 5: 1, 3: 2}
# [2, 3]
