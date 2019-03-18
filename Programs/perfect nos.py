#code
n=int(input())
for i in range(n):
    num=int(input())
    test=0
    for j in range(1,num):
        if (num%j==0):
            test=test+j
    if test==num:
        print("1")
    else:
        print('0')
            
