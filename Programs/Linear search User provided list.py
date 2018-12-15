arr=[int(x) for x in input().split()]  #user provided array list
print(arr)
k=int(input())                         #user provided element to search in arry  


def findNumber(arr, k):
       
   for i in range(len(arr)):
          if arr[i] == k:
                 return True
   return False     
if findNumber(arr,k):
       print("y")
else:
       print("n")

              
                  
                  
       

