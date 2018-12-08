nums=[4,3,5,6,7,8]
def sort(nums):
       for i in range(5):
              
              minpos=i
              for j in range(i,6):
                      if nums[j]<nums[minpos]:
                             minpos=j
              temp=nums[i]
              nums[i]=nums[minpos]
              nums[minpos]=temp
       
              
              
                      
sort(nums)
print(nums)

              
