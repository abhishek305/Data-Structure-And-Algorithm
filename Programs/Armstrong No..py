n=int(input())
for i in range(n): #loop for testcases
    num=int(input())
    sum=0
    temp=num
    while(temp>0):
        d=temp%10
        sum+=d**3
        temp//=10
        
    if num==sum:
        print("Yes")
    else:
        print("No")
        
    
    
