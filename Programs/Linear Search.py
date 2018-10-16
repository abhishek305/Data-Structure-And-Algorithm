
list=[1,3,5,6,9,2]
n=1



def search(list,n):
    i=0
    for i in range(len(list)):
        if list[i] == n:
            return True

    return False
    


if search(list,n):
    print("found")
else:
    print("not found")    
 
