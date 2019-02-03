nums=[1,2,3,4,5]
target=9
def sum_two(nums,target):
    
    if len(nums) <= 1:
        return False
    aux={}
    for i in range(len(nums)):
        if nums[i] in aux:
            return [aux[nums[i]],i]
        else:
            aux[target - nums[i]] =i
print(sum_two(nums,target))            
            
            
        
       
        
